# basedpyright-pre-commit-mirror

## usage

add this to your `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/DetachHead/basedpyright-pre-commit-mirror
    rev: v1.13.0  # or whatever the latest version is at the time
    hooks:
    - id: basedpyright
```

to ensure that basedpyright is able to find all of the dependencies in your
virtual env, add the following to your `pyproject.toml`:

```toml
[tool.basedpyright]
# ...
venvPath = "."
```

## should i use this?

we don't recommend pre-commit as there are better alternatives to it for most of the problems it aims to solve. also the guy who runs it is notorious for being stubborn and unhelpful to users.

we will continue to support pre-commit, however there are alternative approaches you may want to consider depending on your use case:

### checking your code before committing

we instead recommend [integrating basedpyright with your IDE](https://docs.basedpyright.com/#/installation?id=ides). doing so will show errors on your code as you write it, instead of waiting until you go to commit your changes.

### running non-python tools in a python project

pre-commit can be useful when the tool does not have a pypi package, because it can automatically manage nodejs and install npm packages for you without you ever having to install nodejs yourself. [basedpyright already solves this problem with pyright by bundling the npm package as a pypi package](https://docs.basedpyright.com/#/?id=published-as-a-pypi-package-no-nodejs-required).

### running basedpyright in the CI

basedpyright already [integrates well with CI by default](https://docs.basedpyright.com/#/?id=improved-integration-with-ci-platforms) when using the pypi package.