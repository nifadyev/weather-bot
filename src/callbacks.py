from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from telegram.helpers import escape_markdown

from weather_services import retrieve_weather_info

weather_today_template = (
    "\\<emoji placeholder\\> *{description}* \n"
    "Temperature: {morning_feels_like} ℃/ {day_feels_like} ℃/ {night_feels_like} ℃ \n"
    "UV Index: {uv_index} \n"
    "Humidity: {humidity}%\n"
    "Wind: {wind_speed} M/sec\n"
    "Alerts \\[{alerts_count}\\]{first_alert_description}"
)


async def today_weather(context: ContextTypes.DEFAULT_TYPE):
    weather_data = await retrieve_weather_info()
    today_weather_info = weather_data["today"]

    message = weather_today_template.format(
        description=today_weather_info["description"].title(),
        morning_feels_like=int(today_weather_info["morning_feels_like"]),
        day_feels_like=int(today_weather_info["day_feels_like"]),
        night_feels_like=int(today_weather_info["night_feels_like"]),
        uv_index=escape_markdown(str(today_weather_info["uv_index"]), version=2),
        humidity=today_weather_info["humidity"],
        wind_speed=escape_markdown(str(today_weather_info["wind_speed"]), version=2),
        alerts_count=len(weather_data["alerts"]),
        first_alert_description=(
            f': {weather_data["alerts"][0]["description"]}'.title()
            if weather_data["alerts"]
            else ""
        ),
    )

    await context.bot.send_message(
        chat_id=context.job.chat_id, text=message, parse_mode=ParseMode.MARKDOWN_V2
    )
