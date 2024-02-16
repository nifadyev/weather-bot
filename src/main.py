import os
from typing import Final, NoReturn
from telethon import TelegramClient
from telethon.events import NewMessage, StopPropagation
from dotenv import load_dotenv

load_dotenv()

API_ID: Final[int] = int(os.environ["TELEGRAM_API_ID"])
API_HASH: Final[str] = os.environ["TELEGRAM_API_HASH"]
BOT_TOKEN: Final[str] = os.environ["TELEGRAM_BOT_TOKEN"]
bot: TelegramClient = TelegramClient(session="bot", api_id=API_ID, api_hash=API_HASH).start(
    bot_token=BOT_TOKEN
)


@bot.on(event=NewMessage())
async def echo(event: NewMessage.Event):
    await event.respond(event.text)


@bot.on(event=NewMessage(pattern="/example"))
async def example(event: NewMessage.Event) -> NoReturn:
    await event.respond("Hi!")
    raise StopPropagation


def main() -> None:
    bot.run_until_disconnected()


if __name__ == "__main__":
    main()
