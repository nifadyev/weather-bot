import os
from telethon import TelegramClient
from telethon.events import NewMessage
from dotenv import load_dotenv

from telegram.commands import current_forecast, now_is_pressed, start

load_dotenv()


def _init_client() -> TelegramClient:
    return TelegramClient(
        session="bot",
        api_id=int(os.environ["TELEGRAM_API_ID"]),
        api_hash=os.environ["TELEGRAM_API_HASH"],
    ).start(bot_token=os.environ["TELEGRAM_BOT_TOKEN"])


def _add_event_handlers(client: TelegramClient) -> None:
    client.add_event_handler(callback=start, event=NewMessage(pattern="/start"))
    client.add_event_handler(
        callback=current_forecast, event=NewMessage(pattern="/now")
    )
    client.add_event_handler(
        callback=now_is_pressed, event=NewMessage(pattern=r"Now$")
    )
    # bot.build_reply_markup - for building keyboard with buttons


def main() -> None:
    bot = _init_client()

    _add_event_handlers(bot)

    bot.run_until_disconnected()


if __name__ == "__main__":
    main()
