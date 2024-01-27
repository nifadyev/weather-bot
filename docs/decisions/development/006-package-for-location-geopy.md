---
status: accepted
---

# ADR-006: Choose package for working with location services - geopy

## Context and Problem Statement

In order to deal with `US-5`, package for working with location services is required. It should convert city name to coordinates and backwards. Coordinates are necessary for OpenWeatherMap API requests. It should support at least Python 3.11.

## Considered Options

* geopy

## Decision Outcome

**Chosen option**: `geopy`, because
it is able to solve desired tasks and it actually does not have any alternative.

## Pros and Cons of the Options

### geopy

[github](https://github.com/geopy/geopy)

* Good, because is supports many geocoding services
* Good, because it is tested on Python 3.12
* Neutral, because has some dependencies
