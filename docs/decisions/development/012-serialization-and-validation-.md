---
status: accepted
---

# ADR-012: Choose package for serialization and validation - msgspec

## Context and Problem Statement

The system will interact with third party API - OpenWeatherMap API. Due to that fact, a tool for data validation and serialization is required.

This tool should support dataclasses (or schema) based validation, because it's not convenient to work with raw JSON (no validation and typing), be lightweight, because it is a small system part, and be configurable for specific cases.

## Considered Options

* pydantic
* msgspec
* catts
* mashumaro

## Decision Outcome

**Chosen option**: "msgspec", because
it is dependencies-free, integrates well with type checkers and IDEs and it is backed by Litestart (modern async framework)

## Pros and Cons of the Options

### pydantic

Rust based, [documentation](https://docs.pydantic.dev/latest/)

* Good, because development team is familiar with it (used in V1)
* Good, because it a part of large ecosystem (fastapi, plugins, integrations)
* Good, because it is mature project with 2 major versions, well written documentation and community
* Neutral, because it generates JSON Schema for API documentation
* Neutral, because it has few dependencies
* Bad, because it has a lot of implicit logic. For example, during validation

### msgspec

[documentation](https://jcristharif.com/msgspec/)

* Good, because it does not have dependencies
* Good, because it uses standard type annotations
* Good, because it is the fastest package in average task. It is even faster than Rust-based `pydantic` V2
* Good, because it integrates well with common type checkers (`mypy`, `pyright`)
* Neutral, because it also support MessagePack, YAML, TOML. OWM API only supports JSON, so it is not important
* Bad, because it is quite new (created at 2021) and does not have any major release

### catts

Library for structuring and unstructuring data
[Comparison with Pydantic](https://threeofwands.com/why-i-use-attrs-instead-of-pydantic/)

* Good, because it tries to avoid implicit logic as much as possible. Developer should have almost full control
* Good, because it has well written documentation
* Good, because it is mature project (started from 2016) and has community and StackOverflow questions
* Neutral, because it has some dependencies
* Neutral, because it also support MessagePack, YAML, TOML. OWM API only supports JSON, so it is not important
* Bad, because it has hard to configure validation. It's just a guess based on lack of information in documentation

### mashumaro

[github](https://github.com/Fatal1ty/mashumaro)

* Good, because it also generate JSON Schema
* Good, because it is mature project with 3-rd major version, well written documentation and community. Also it has a few issues
* Good, because it uses standard type annotations
* Good, because it integrates well with common type checkers (`mypy`, `pyright`)
* Neutral, because it also support MessagePack, YAML, TOML. OWM API only supports JSON, so it is not important
* Bad, because based on quick documentation overview it is overkill for project's purposes

## More Information

The choice was very difficult because most packages suits for project purposes. Maybe the chosen package is not mature enough but it is definitely worth trying.
