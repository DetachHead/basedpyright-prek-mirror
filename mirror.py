import subprocess
from pathlib import Path

import tomli
import tomli_w
import urllib3
from packaging.requirements import Requirement
from packaging.version import Version


def main():
    with open(Path(__file__).parent / "pyproject.toml", "rb") as f:
        pyproject = tomli.load(f)

    # get current version of basedpyright
    deps = pyproject["project"]["dependencies"]
    assert len(deps) == 1
    basedpyright_dep = Requirement(deps[0])
    assert basedpyright_dep.name == "basedpyright"
    basedpyright_specs = list(basedpyright_dep.specifier)
    assert len(basedpyright_specs) == 1
    assert basedpyright_specs[0].operator == "=="
    current_version = Version(basedpyright_specs[0].version)

    # get all versions of basedpyright from PyPI
    resp = urllib3.request("GET", "https://pypi.org/pypi/basedpyright/json")
    if resp.status != 200:
        raise RuntimeError

    versions = [Version(release) for release in resp.json()["releases"]]
    versions = [v for v in versions if v > current_version and not v.is_prerelease]
    versions.sort()

    for version in versions:
        pyproject["project"]["dependencies"] = [f"basedpyright=={version}"]
        with open(Path(__file__).parent / "pyproject.toml", "wb") as f:
            tomli_w.dump(pyproject, f)
        subprocess.run(["git", "add", "pyproject.toml"])
        subprocess.run(["git", "commit", "-m", f"basedpyright {version}"])
        subprocess.run(["git", "tag", f"{version}"])


if __name__ == "__main__":
    main()
