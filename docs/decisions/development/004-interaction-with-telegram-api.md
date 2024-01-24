---
status: proposed
---

# ADR-004: Protocol for interacting with Telegram API - MTProto

## Context and Problem Statement

Communication with Telegram API could be implemented using various protocols.
The solution should use network resources wisely, it should be maintainable and easy to configure.

## Considered Options

* polling
* webhook
* MTProto

## Decision Outcome

**Chosen option**: MTProto, because it is direct protocol for using Telegram API, it saves networks resources and give more functions than webhooks (but probably harder to configure)

## Pros and Cons of the Options

### polling

Periodically send requests to Telegram servers to get information about recent activity. If something is found, then interaction with bot is started

* Good, because it is the easiest protocol for quick start
* Neutral, because it is simply an HTTP endpoint which translates requests into MTProto calls
* Bad, because it uses network resources in vain

### webhook

Telegram itself call event/message handler when there is some activity in bot.

* Good, because it instantly send response
* Neutral, because it is simply an HTTP endpoint which translates requests into MTProto calls
* Neutral, because it requires endpoint, SSL and static IP to configure
* Bad, because server is prone to unexpected requests, users and bots

### MTProto

MTProto is Telegram’s own protocol to communicate with their API when you connect to their servers.

* Good, because does not require setting up endpoint, web framework
* Good, because it much faster than other options. It's direct calls to Telegram servers
* Good, because it gives full control over Text Entities. For example, format messages using more than HTML or Markup
* Neutral, because it allow bulk delete messages
* Bad, because it is (possibly) hard to configure
* Bad, because it is proprietary Telegram protocol which could be unexpectedly changed or abandoned

## More Information

### Links

* [MTProto Telephon overview](https://docs.telethon.dev/en/stable/concepts/botapi-vs-mtproto.html)
* [MTProto compared with HTTP Bot API](https://github.com/LonamiWebs/Telethon/wiki/MTProto-vs-HTTP-Bot-API)
* [Webhook python-telegram-bot example](https://docs.python-telegram-bot.org/en/stable/examples.customwebhookbot.html)
* [Webhooks - python-telegram-bot Wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks)
* [Guide to All Things Webhook - Telegram Docs](https://core.telegram.org/bots/webhooks)
* [Why Webhook is preferred over Polling in Telegram bots? - Ru Habr](https://habr.com/ru/companies/otus/articles/786754/)
