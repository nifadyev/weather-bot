from typing import NoReturn
from telethon import Button
from telethon.events import NewMessage, StopPropagation

from constants.messages import START_MESSAGE

from owm_api import retrieve_weather_info
from renderers import render_current_forecast


async def start(event: NewMessage.Event) -> NoReturn:
    if not event.chat_id:
        raise

    if not event.client:
        raise

    await event.client.send_message(
        entity=event.chat_id,
        message=START_MESSAGE,
        buttons=[
            [
                Button.text("Now", resize=True),
                Button.text("Today", resize=True),
                Button.text("Tomorrow", resize=True),
            ],
            [
                Button.text("Week", resize=True),
                Button.text("Schedule forecast", resize=True),
                Button.text("Settings", resize=True),
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
        entity=event.chat_id, message=formatted_forecast_template,
    )

    raise StopPropagation


async def now_is_pressed(event) -> NoReturn:
    await current_forecast(event)
