# Development details

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
