---
status: accepted
---

# ADR-013: Choose logging package - structlog

## Context and Problem Statement

Log messages are required to quickly inspect errors and the reasons why they happened.
Logger should be descriptive (more useful stack trace and artifacts), configurable and does not require many lines of code.

## Considered Options

* logging
* loguru
* structlog
* eliot

## Decision Outcome

**Chosen option**: "structlog", because
it allows saving structured logs with context. It is not so popular as `loguru`, which has partually the same feature for log structuring, and not "inventing a wheel" as `eliot`, but it is mature enough to try. `logging` is just a familiar and known package but it was decided to try something new since the project allows it.

## Pros and Cons of the Options

### logging

* Good, because it is de-facto standard Python logger
* Good, because development team is familiar with it
* Neutral, because it uses old `%` string formatting

### loguru

[github](https://github.com/Delgan/loguru)

* Good, because it uses the concept of one logger instead of one logger per one module
* Good, because it has descriptive exceptions with stack trace
* Good, because it is usable out-of-the-box without much configuration
* Good, because it is asynchronous and thread-safe
* Neutral, because it uses modern `{}` string formatting
* Neutral, because it supports structured logs

### structlog

[guide](https://betterstack.com/community/guides/logging/structlog/)

* Good, because it does not have dependencies
* Good, because supports both classic string logging and structured logging with context
* Neutral, because it uses old `%` string formatting. It is said to be faster than `{}` formatting but f-strings are also supported

### eliot

[documentation](https://eliot.readthedocs.io/en/stable/quickstart.html)

* Good, because it is the logger that tells why something happened
* Neutral, because it is new logging concept and there is not enough information about it
* Bad, because it is hard to setup and it will possibly consume a lot of time to configure
