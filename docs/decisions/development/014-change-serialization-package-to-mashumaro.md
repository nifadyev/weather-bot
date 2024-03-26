---
status: accepted
---

# ADR-014: Change serialization package - mashumaro

## Context and Problem Statement

major issues occurred during adopting `pydantic` based schemas to `msgspec`. It turned out that `msgspec` does not convert fields during deserialization if field alias is defined.

The replacement should support missing `msgspec` features and optionally support validation. Validation is not required because data is coming from third party API and raised error will be the mark of API changes.

## Considered Options

* attrs
* cattrs
* mashumaro

## Decision Outcome

Chosen option: "mashumaro", because
it is the only considered option which fits in requirements. It does not have a validation but for now there is no use case to validate.

## Pros and Cons of the Options

### attrs

The basis for many serialization packages like `cattrs`, `msgspec`, etc.

* Good, because it is does not have dependencies
* Good, because it is the core of many alternative packages
* Bad, because it cannot handle nested JSON
* Bad, because it cannot ignore unnecessary fields out of the box (but there is a workaround)

### cattrs

Extension of `attrs` with some advanced features.

* Bad, because it cannot handle both field alias and field converter
* Bad, because converter is ran before validator

### mashumaro

In addition to information from [ADR-012](012-serialization-and-validation-msgspec.md)

* Good, because it can handle both field alias and converter
* Good, because it is tightly coupled with standard `dataclasses`
* Bad, because it does not have built-in validation

## More Information

`msgspec` can possibly solve the problem but it will require 2 schemas: input and output. In my opinion, it is a bad hack.
