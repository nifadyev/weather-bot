# Development details

## Project structure

Use [this new](https://github.com/sourcery-ai/python-best-practices-cookiecutter/tree/main/%7B%7Bcookiecutter.repo_name%7D%7D) and [this old](https://github.com/audreyfeldroy/cookiecutter-pypackage/tree/master/%7B%7Bcookiecutter.project_slug%7D%7D) `cookiecutter` templates for reference

Based on ADRs, the project will be followed like this:

- .github/ - stores PR, issues templates, Github Actions workflows
- docs/ - the only place with documentation. Follows Docs as a Code approach
- src/
  - weather_provider/ - OpenWeatherMap API related logic, including data serialization and validation and requests to API
  - templates/ - message templates
  - telegram/ - interaction with Telegram API
  - geo/ - logic for dealing with user location
  - constants.py
  - config.py or settings.py - project settings, for example loading `.env` file (maybe move to main.py)
  - main.py or app.py - enter point to the project, configure and run server
- tests/
- other service files and configs like `docker-compose.yml`, `Makefile`, `.pre-commit-config.yaml`, etc.

## Testing

[How to write tests for Telegram bot - ptb](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Writing-Tests)
[Simple test example - Telethon](https://docs.telethon.dev/en/stable/developing/testing.html)

Use [pytest-randomly](https://github.com/pytest-dev/pytest-randomly) and [pytest-repeat](https://github.com/pytest-dev/pytest-repeat) to avoid flaky tests. The last tool could be run only on pre-commit in order to save time.

Steps after MVP - mutation tests, proper integration tests

### What is unit test?

Unit tests should cover all logic without external dependencies. It could be validators, serializers, converters and message formatters. For now mocks are avoidable until better alternative is chosen and adopted.

Start with basic unit tests and then try to adopt `Hypothesis` property-based testing [guide](https://semaphoreci.com/blog/property-based-testing-python-hypothesis-pytest)

### What is integration test?

Tests with imitation of actual behavior. They will mostly cover interaction with OWM API and Telegram.

Will not be implemented until MVP.

## Type Checking

The project should be statically typed from the beginning. Development team has experience with typing existing codebase and it always ended on incomplete state. System is working so why bothering with types?!

That is why system will be strictly typed by default.
