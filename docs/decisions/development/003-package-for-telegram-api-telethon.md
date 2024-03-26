---
status: accepted
---

# ADR-003: Choose package for Telegram API interaction - Telethon

## Context and Problem Statement

Since Telegram is chosen as "frontend" of the system, it is necessary to pick an option for interacting with API. Option should be up-to-date, well documented, lightweight and easy to use

## Considered Options

* [python-telegram-bot](https://docs.python-telegram-bot.org/en)
* [aiogram](https://docs.aiogram.dev/en/latest/index.html)
* [Telethon](https://github.com/LonamiWebs/Telethon/tree/v1)
* [pyrogram](https://github.com/pyrogram/pyrogram)
* pyTelegramBotAPI
* direct API calls

## Decision Outcome

**Chosen option**: "Telethon", because it's based on `MTProto`, it will not require overhaul during webhook installation and it's well documented and up-to-date.

### Consequences

* Good, because allow to use modern way of communication with Telegram servers
* Bad, because it will require more time to inspect documentation and migrate from current package

## Pros and Cons of the Options

### python-telegram-bot

* Good, because it is familiar for development team
* Good, because it has only 1 external dependency - `httpx`. Other dependencies for HTTP2, webhooks and scheduling are optional
* Good, because it has well written documentation with a lot of examples and solutions (for example, bot testing)
* Neutral, because it requires [tornado](https://www.tornadoweb.org/en/stable/) Web Framework for webhook support (see ADR-004 for details)

### aiogram

* Good, because it has type hints
* Good, because it has integrated I18n/L10n support
* Neutral, because it requires `aiohttp` Web Framework for webhook support
* Neutral, because it is mostly the same as familiar `python-telegram-bot`
* Bad, because it has toxic community

### Telethon

* Good, because it based on MTProto (see ADR-004 for details)
* Good, because it has well-written documentation
* Neutral, because it uses SQLite by default for session storage
* Neutral, because it supports [scheduled functions](https://github.com/LonamiWebs/Telethon/wiki/Scheduling-Functions) via `asyncio` or `apscheduler`
* Neutral, because it could use [cryptg](https://docs.telethon.dev/en/stable/basic/installation.html#optional-dependencies) to speed up encryption/decryption on C instead of Python
* Neutral, because it possibly supports message [translation](https://tl.telethon.dev/methods/messages/translate_text.html)
* Neutral, because it does not have useful helper to escape reserved Markdown symbols (like `escape_markdown` in `python-telegram-bot`)
* Bad, because it will require more time to develop using new techniques and `asyncio` studying

### pyrogram

* Good, because it is based on MTProto
* Bad, because it seems to be [abandoned](https://github.com/pyrogram/pyrogram/issues/1382) and not updated for more than 9 months

### pyTelegramBotAPI

* Good, because it is used by many projects
* Good, because it is up-to-date
* Neutral, because it supports webhooks
* Bad, because its documentation is not detailed

## More Information

Revisit this decision before writing any code. It should be confirmed that chosen package is able to deal with chosen decisions.

### Links

* [Migration guide from other packages](https://docs.telethon.dev/en/stable/concepts/botapi-vs-mtproto.html#id5)
* [Examples](https://github.com/LonamiWebs/Telethon/tree/v1/telethon_examples)
* [Project using this package](https://github.com/LonamiWebs/Telethon/wiki/Projects-using-Telethon)
