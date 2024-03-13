import os
from typing import Final, NoReturn
from telethon import Button, TelegramClient
from telethon.events import NewMessage, StopPropagation
from dotenv import load_dotenv
from telethon import events

from constants.messages import START_MESSAGE

load_dotenv()

API_ID: Final[int] = int(os.environ["TELEGRAM_API_ID"])
API_HASH: Final[str] = os.environ["TELEGRAM_API_HASH"]
BOT_TOKEN: Final[str] = os.environ["TELEGRAM_BOT_TOKEN"]
bot: TelegramClient = TelegramClient(
    session="bot", api_id=API_ID, api_hash=API_HASH
).start(bot_token=BOT_TOKEN)


@bot.on(event=NewMessage(pattern="/example"))
async def example(event: NewMessage.Event) -> NoReturn:
    await event.respond("Hi!")

    raise StopPropagation


@bot.on(event=NewMessage(pattern="/start"))
async def start(event: NewMessage.Event) -> NoReturn:
    if not event.chat:
        raise

    await bot.send_message(
        entity=event.chat,
        message=START_MESSAGE,
        buttons=[
            [
                Button.inline(text="Now"),
                Button.inline(text="Today"),
                Button.inline(text="Tomorrow"),
            ],
            [
                Button.inline(text="Week"),
                Button.inline(text="Schedule forecast"),
                Button.inline(text="Settings"),
            ],
        ],
    )

    raise StopPropagation


@bot.on(events.CallbackQuery(pattern="Now"))
async def now_is_pressed(event) -> NoReturn:
    await example(event)


def main() -> None:
    bot.run_until_disconnected()


if __name__ == "__main__":
    main()
