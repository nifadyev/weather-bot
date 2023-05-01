from datetime import time

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from callbacks import today_weather
from src.constants import DAILY_FORECAST_UTC_HOUR
from weather_services import retrieve_weather_info

weather_now_template = (
    "\\<emoji placeholder\\> *{description}* \n"
    "*Feels like*: {current_feels_like} ℃ \n"
    "Today: {today_morning_feels_like} ℃/ {today_day_feels_like} ℃/ {today_night_feels_like} ℃ \n"
    "Today weather: {today_description} \n"
    "Alerts \\[{alerts_count}\\]{first_alert_description}"
)


# /start - begins the interaction with the user, like sending an introductory message. This command can also be used to pass additional parameters to the bot (see Deep Linking).
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Weather bot!")


# /help - returns a help message, like a short text about what your bot can do and a list of commands.
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Please use Menu to see available commands"
    )


async def now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    weather_data = await retrieve_weather_info()
    message = weather_now_template.format(
        current_feels_like=int(weather_data["now"]["feels_like"]),
        today_morning_feels_like=int(weather_data["today"]["morning_feels_like"]),
        today_day_feels_like=int(weather_data["today"]["day_feels_like"]),
        today_night_feels_like=int(weather_data["today"]["night_feels_like"]),
        today_description=weather_data["today"]["description"].title(),
        description=weather_data["now"]["description"].title(),
        alerts_count=len(weather_data["alerts"]),
        first_alert_description=(
            f': {weather_data["alerts"][0]["description"]}'.title()
            if weather_data["alerts"]
            else ""
        ),
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.MARKDOWN_V2
    )


async def enable_daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id, text="Daily weather forecast is enabled")

    context.job_queue.run_daily(today_weather, time=time(hour=DAILY_FORECAST_UTC_HOUR), chat_id=chat_id)
