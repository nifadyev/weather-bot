---
status: accepted
---

# ADR-010: Choose task runner - make

## Context and Problem Statement

Project requires some tool to run often commands as tasks, not as separate `bash` commands. Task runners are also helpful during CI and initial local setup. All necessary commands in one place.
Task runner should be simple, support many platforms out-of-the-box and be clear for most developers.

## Considered Options

* make
* just
* task

## Decision Outcome

**Chosen option**: make, because
it is built-in in all Unix distros and familiar to vast majority of developers.

## Pros and Cons of the Options

### make

* Good, because it is de-facto standard for dealing with tasks
* Good, because it is built in in most Unix distros
* Good, because it has large community and a lot of guides and tutorials
* Neutral, because it does not support Windows. Development team does not this OS, so not critical
* Bad, because it is initially build system, not a task runner, and many hacks are required during configuration
* Bad, because it does not support loading variables from `.env` file

### just

Rust based, [github](https://github.com/casey/just)

* Good, because it is cross-platform
* Good, because it supports loading variables from `.env` file
* Good, because it supports writing tasks on other languages (Python included)
* Neutral, because it has mostly the same format as `make`
* Bad, because it should be installed as a standalone system package (not built-in)

### task

Go based, [github](https://github.com/go-task/task)

* Good, because it is cross-platform
* Neutral, because it uses YML for writing tasks
* Bad, because it should be installed as a standalone system package (not built-in)
