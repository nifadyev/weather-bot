from datetime import time
from typing import Coroutine

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from callbacks import today_weather
from constants import (
    DAILY_FORECAST_UTC_HOUR,
    ENABLE_DAILY_COMMAND,
    ICON_ID_TO_EMOJI,
    NOW_COMMAND,
    NOW_WEATHER_TEMPLATE,
)
from weather_services import retrieve_weather_info

MENU_MARKUP = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Current weather", callback_data=NOW_COMMAND),
            InlineKeyboardButton(text="Enable daily forecast", callback_data=ENABLE_DAILY_COMMAND),
        ]
    ],
)


# /start - begins the interaction with the user, like sending an introductory message. This command can also be used to pass additional parameters to the bot (see Deep Linking).
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welcome to Weather bot!",
        reply_markup=MENU_MARKUP,
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show menu with available commands."""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Choose command below",
        reply_markup=MENU_MARKUP,
    )


# /help - returns a help message, like a short text about what your bot can do and a list of commands.
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Please use Menu to see available commands"
    )


async def now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    weather_data = await retrieve_weather_info()
    message = NOW_WEATHER_TEMPLATE.format(
        current_feels_like=weather_data.current.feels_like,
        today_morning_feels_like=weather_data.daily[0].feels_like.morning,
        today_day_feels_like=weather_data.daily[0].feels_like.day,
        today_night_feels_like=weather_data.daily[0].feels_like.night,
        today_description=weather_data.daily[0].summary,
        today_icon=ICON_ID_TO_EMOJI.get(
            weather_data.daily[0].weather[0].icon_id, ICON_ID_TO_EMOJI["default"]
        ),
        description=weather_data.current.weather[0].description,
        icon=ICON_ID_TO_EMOJI.get(
            weather_data.current.weather[0].icon_id, ICON_ID_TO_EMOJI["default"]
        ),
        alerts_count=len(weather_data.alerts),
        first_alert_description=(
            f": {weather_data.alerts[0].description}" if weather_data.alerts else ""
        ),
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.MARKDOWN_V2
    )


async def enable_daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id, text="Daily weather forecast is enabled")

    context.job_queue.run_daily(
        today_weather, time=time(hour=DAILY_FORECAST_UTC_HOUR), chat_id=chat_id
    )


async def button_tap(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Coroutine | None:
    """Parse and process tapping on inline buttons on the menu."""
    # TODO: Make common decorator with raise for all handlers with Update (separate for context)
    if not update.callback_query:
        return

    data = update.callback_query.data

    if data == NOW_COMMAND:
        await now(update, context)
    elif data == ENABLE_DAILY_COMMAND:
        await enable_daily(update, context)

    # Close the query to end the client-side loading animation
    await update.callback_query.answer()
