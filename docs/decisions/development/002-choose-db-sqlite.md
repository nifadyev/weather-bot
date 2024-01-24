---
status: proposed
---

# ADR-002: Choose DB - SQLite

## Context and Problem Statement

System requires persistent storage to save user settings and user data between system restarts and failures.

## Considered Options

* SQLite
* PostgreSQL
* Do not store persistent data

## Decision Outcome

**Chosen option**: "SQLite", because it is easy to set up and use, also it is not difficult to migrate to another DB service. PostgreSQL would be too much at current stage but system requires DB anyway or user experience will suffer.
