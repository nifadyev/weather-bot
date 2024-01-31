---
status: accepted
---

# ADR-009: Forecast content

## Context and Problem Statement

Forecast should be short but filled with useful details. It should be clear for common user.

## Considered Options

* Weather condition
* Wind
* Humidity
* UV Index
* Alerts
* Current weather specifics
* Daily weather specifics
* Weekly weather specifics

## More Information

### Weather condition

* OWM API provides 2 options for text description - `summary` and `description`. Summary is english only and more detailed and description is localized but lacks some details. Anyway, decision outcome is `description` because localization is planned in `US-5`

### Wind

* OWM API provides 2 related fields - `wind_speed` and `wind_direction`. Both of them are useful but `wind direction` should be converted to human readable value like `south/north-east/etc`. This task has low priority and could be performed later.

### Humidity

* OWM API provides humidity as percent which is totally fine to use as is

### UV Index

* OWM API provide float value. It should be converted to int. Separate low priority task is to add warning and recommendations when high values are reached (in case `alerts` section is empty)

### Alerts

* OWM API provides optional localized `alerts` section. The content could be displayed as only 1 alert or extra button to list all alerts (low priority task)

### Current weather specifics

* Current weather forecast should contain all information from daily weather and additionally current `feels like` and current `description`

### Daily weather specifics

* Weather forecast should contain `icon`, localized weather condition `description`, `feels like` (morning, day, evening, on separate lines), `wind`, `humidity`, `uv index` and optional localized `alerts`

### Weekly weather specifics

* Weekly forecast should contain `icon`, localized weather condition `description` and `feels like` (morning, day, evening, on separate lines) for each day
