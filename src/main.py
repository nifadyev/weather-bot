import os
from typing import Final
from telethon import TelegramClient
from telethon.events import NewMessage
from dotenv import load_dotenv
from telethon import events

from telegram.commands import current_forecast, now_is_pressed, start

load_dotenv()

# TODO: Move to some init function and call it in main
API_ID: Final[int] = int(os.environ["TELEGRAM_API_ID"])
API_HASH: Final[str] = os.environ["TELEGRAM_API_HASH"]
BOT_TOKEN: Final[str] = os.environ["TELEGRAM_BOT_TOKEN"]
bot: TelegramClient = TelegramClient(
    session="bot", api_id=API_ID, api_hash=API_HASH
).start(bot_token=BOT_TOKEN)



def main() -> None:
    bot.add_event_handler(callback=start, event=NewMessage(pattern="/start"))
    bot.add_event_handler(callback=current_forecast, event=NewMessage(pattern="/now"))
    bot.add_event_handler(callback=now_is_pressed, event=events.CallbackQuery(pattern="Now"))

    bot.run_until_disconnected()


if __name__ == "__main__":
    main()
