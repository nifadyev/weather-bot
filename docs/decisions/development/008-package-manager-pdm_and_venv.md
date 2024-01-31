---
status: accepted
---

# ADR-008: Choose package manager - pdm + venv

## Context and Problem Statement

Each Python project requires package manager for dealing with dependencies and many more tasks.
Suitable manager should be supported by most CI/CD tools and processes, easily build into Docker, actively maintainable and configurable.

## Considered Options

* poetry
* pip
* pdm

## Decision Outcome

**Chosen option**: "pdm without internal venv", because
such tool should not be "the tool to rule them all", it will just produce more errors. `pdm` is preferred over `poetry` mostly because of number of issues and bad feedback about `poetry` from devs.
`pip` is not chosen because it lacks some necessary features and development team has unpleasant experience with it.

## Pros and Cons of the Options

### poetry

[docs](https://python-poetry.org/docs/)

* Good, because it uses modern `pyproject.toml` and `*.lock` way of storing dependencies
* Good, because it can manage virtual environments
* Neutral, because it allows grouping dependencies
* Neutral, because it also helps with building and packaging
* Bad, because it has more than 600 open issues (February 2024)
* Bad, because there are difficulties with installing in Docker/CI
* Bad, because devs previously pushed breaking changes as patch version. It changed the format of critical files and broke CI pipelines. Also, they randomly raised exception in CI to force an upgrade from v1 to v2

### pip

* Good, because it is de-facto standard Python package manager
* Good, because it does not require extra steps in CI/CD and Docker configuration
* Neutral, because dependencies could be grouped by having different `requirements` files
* Bad, because uses of way of storing dependencies (`txt`)
* Bad, because does lock package versions. Packages which are necessary only for another package, will not be saved anywhere
* Bad, because it does not show dependencies tree

### pdm

[awesome-pdm](https://github.com/pdm-project/awesome-pdm)

SUpport VSCode?

* Good, because it uses modern `pyproject.toml` and `*.lock` way of storing dependencies
* Good, because it has good documentation
* Neutral, because it follows [PEP 621](https://www.python.org/dev/peps/pep-0621) toml file structure
* Bad, because it is pretty new (small community, not many StackOverflow questions, not polished)

## More Information

[Relieving your Python packaging pain](https://www.bitecode.dev/p/relieving-your-python-packaging-pain) - helpful article which describes common problems with dependency management
[Why not tell people to "simply" use pyenv, poetry or anaconda](https://www.bitecode.dev/p/why-not-tell-people-to-simply-use) - article with good point about not over complicating things and just use the defaults. The reason is mostly because other tools have too many modes of failure, while solving problems that people won’t have as long as they are battling more primitive issues.

Other tools like [pip-tools](https://github.com/jazzband/pip-tools) and [rye](https://rye-up.com/) are considered not suitable based on quick review. The first one is supercharged `pip` and the second one is `Rust` based and its maintainer advised `pdm` as go-to solution.
