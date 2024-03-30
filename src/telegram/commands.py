from typing import NoReturn
from telethon import Button
from telethon.events import NewMessage, StopPropagation

from constants.messages import START_MESSAGE

from owm_api import retrieve_weather_info
from renderers import render_current_forecast


async def start(event: NewMessage.Event) -> NoReturn:
    # TODO: decorator with common check
    if not event.chat_id:
        raise

    if not event.client:
        raise

    await event.client.send_message(
        entity=event.chat_id,
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


async def current_forecast(event: NewMessage.Event) -> NoReturn:
    if not event.chat_id:
        raise
    if not event.client:
        raise

    forecast = await retrieve_weather_info()
    formatted_forecast_template = render_current_forecast(forecast)

    await event.client.send_message(
        entity=event.chat_id, message=formatted_forecast_template
    )

    raise StopPropagation


async def now_is_pressed(event) -> NoReturn:
    await current_forecast(event)
