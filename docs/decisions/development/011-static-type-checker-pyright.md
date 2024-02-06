---
status: accepted
---

# ADR-011: Choose type checker - pyright

## Context and Problem Statement

Speed is not a top priority, type checker should has less errors and false positive, well maintainable, with good documentations and support. It also should have option to forbid `Any` type.

## Considered Options

* mypy
* pyright
* pylyzer
* beartype

## Decision Outcome

**Chosen option**: "pyright", because
it does not have many unresolvable `mypy` issues, has decent performance and incredible VS Code integration.
`pylyzer` is too "raw" and its performance is not necessary on this project.
`beartype` looks promising but it integrates well with static type checkers and could be added on next development phases.

## Pros and Cons of the Options

### mypy

* Good, because it is de-facto standard Python type checker
* Good, because it has good IDE support and many plugins for `pytest`
* Good, because it has `strict` flag to forbid running code with type errors
* Neutral, because it is designed with gradual typing in mind. Not relevant to this project
* Bad, because it slower than alternatives

### pyright

[Differences from mypy](https://microsoft.github.io/pyright/#/mypy-comparison)

* Good, because it has `strict` flag to forbid running code with type errors
* Good, because it tries to assume return type by using `return` or `yield` while `mypy` always assumes `Any`
* Good, because it is also language server with auto completion and many more functions
* Neutral, because it designed for large codebases. Not a case of this project.
* Neutral, because it does not have plugins. But it is [by design](https://microsoft.github.io/pyright/#/mypy-comparison?id=plugins) and authors have their reasoning
* Neutral, because it works best with VS Code. Dev team uses this IDE but it sounds like a limitation
* Bad, because it developed by Microsoft and could be closed sourced any day or provide Microsoft-specific features

### pylyzer

Rust based, [github](https://github.com/mtshiba/pylyzer)

* Good, because it performs detailed analysis. For example, it can detect out-of-bounds accesses to lists
* Neutral, because it is the fastest option. But it is not necessary for this project. Codebase will not be large
* Neutral, because it is also language server. But it is not backed by huge dev team like `pyright`
* Neutral, because it has potentially many false positives and the approach is conservative
* Bad, because it in beta and have smaller community than `mypy` and `pyright`

### beartype

[documentation](https://beartype.readthedocs.io/en/latest/)

* Good, because third generation type checker (both runtime and static). More info [here](https://beartype.readthedocs.io/en/latest/faq/#third-generation-type-checker-doesn-t-mean-anything-does-it)
* Good, because it requires only 2 lines of code in `__init__.py` to work
* Good, because it has well written documentation
* Good, because it has good IDE support and many plugins for `pytest`
* Bad, because it has not much guides, questions and articles

## More Information

More time dev team spend on reading about typing on Python, more it understands that maybe dynamically typed Python is not their best choice.
