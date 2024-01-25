---
status: accepted
---

# ADR-005: Choose HTTP client for OWM requests - httpx

## Context and Problem Statement

HTTP client is required to communicate with OpenWeatherMap APi. It should be fast, support HTTP/2, async and does not have many dependencies.

## Considered Options

* [httpx](https://www.python-httpx.org/)
* [requests](https://requests.readthedocs.io/en/latest/)

## Decision Outcome

**Chosen option**: httpx, because
it fulfill all requirements for HTTP client.

## Pros and Cons of the Options

### httpx

* Good, because it supports async requests
* Good, because it supports HTTP/2
* Good, because it is fully type annotated
* Neutral, because development team is familiar with it (from V1)
* Neutral, because it supports most of `requests` features because it is based on it
* Bad, because it has many dependencies

### requests

* Good, because de-facto standard package for making HTTP requests in Python world
* Good, because it has zero dependencies
* Neutral, because development team is familiar with it
* Bad, because it does not support async requests
* Bad, because it does not HTTP/2

## More Information

Made quick search for alternatives and haven't found any package that offers more than `httpx`
