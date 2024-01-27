---
status: accepted
---

# ADR-007: Choose linting and formatting tools - ruff

## Context and Problem Statement

Project codebase should be consistent and follow best practices. Tools such linter and auto formatter are here to help. They should be configurable, with huge community, contains many rules and support most of relevant practices and versions (python, type checking, etc.)

## Considered Options

* ruff
* flake8
* black

## Decision Outcome

**Chosen option**: ruff, because
it replaces a lot of tools, it is both linter and formatter and it is actively evolving.
Development team is familiar with all considered options and it does not affect on final decision.

## Pros and Cons of the Options

### ruff

[Website](https://docs.astral.sh/ruff/)

* Good, because it is extremely fast
* Good, because it is also auto formatter and could replace `black`
* Good, because it could auto delete dead code (replaces `eradicate` and [vulture](https://github.com/jendrikseipp/vulture))
* Good, because it replaces `pyupgrade`, `isort` and a lot of useful packages``
* Good, because it has `pre-commit` hook
* Neutral, because it tries to be all-in-one tool and it has too much rules
* Bad, because it is in beta and updated very often

### flake8

[Website](https://flake8.pycqa.org/en/latest/)

* Good, because it is de-facto standard linter in Python community
* Neutral, because it is has a lot of plugins. But it is not easy to find and configure necessary ones
* Neutral, because it is written on Python (mostly related to speed)

### black

[Website](https://black.readthedocs.io/en/stable/)

* Good, because it is extremely fast
* Good, because it is stable
* Neutral, because it poorly configurable

## More Information

Tools are actively evolving and this ADR could be revised later.
