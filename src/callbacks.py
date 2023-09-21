from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from constants import ICON_ID_TO_EMOJI, TODAY_WEATHER_TEMPLATE
from weather_services import retrieve_weather_info


async def today_weather(context: ContextTypes.DEFAULT_TYPE):
    weather_data = await retrieve_weather_info()
    today_weather_info = weather_data.daily[0]

    message = TODAY_WEATHER_TEMPLATE.format(
        icon=ICON_ID_TO_EMOJI.get(
            today_weather_info.weather[0].icon_id, ICON_ID_TO_EMOJI["default"]
        ),
        morning_feels_like=today_weather_info.feels_like.morning,
        day_feels_like=today_weather_info.feels_like.day,
        night_feels_like=today_weather_info.feels_like.night,
        description=today_weather_info.summary,
        uv_index=today_weather_info.uv_index,
        humidity=today_weather_info.humidity,
        wind_speed=today_weather_info.wind_speed,
        alerts_count=len(weather_data.alerts),
        first_alert_description=(
            # TODO: concat alert summary and description because description could be empty
            f": {weather_data.alerts[0].description}".title()
            if weather_data.alerts
            else ""
        ),
    )

    await context.bot.send_message(
        chat_id=context.job.chat_id, text=message, parse_mode=ParseMode.MARKDOWN_V2
    )
