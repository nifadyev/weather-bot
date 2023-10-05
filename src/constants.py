from typing import Final

NOW_COMMAND: Final[str] = "now"
ENABLE_DAILY_COMMAND: Final[str] = "enable_daily"

NOW_WEATHER_TEMPLATE: str = (
    "{icon} *{description}* \n"
    "*Feels like*: {current_feels_like} ℃ \n"
    "Today: {today_morning_feels_like} ℃/ {today_day_feels_like} ℃/ {today_night_feels_like} ℃ \n"
    "Today weather: {today_icon} {today_description} \n"
    "Alerts \\[{alerts_count}\\]{first_alert_description}"
)

TODAY_WEATHER_TEMPLATE: str = (
    "{icon} *{description}* \n"
    "Temperature: {morning_feels_like} ℃/ {day_feels_like} ℃/ {night_feels_like} ℃ \n"
    "UV Index: {uv_index} \n"
    "Humidity: {humidity}%\n"
    "Wind: {wind_speed} M/sec\n"
    "Alerts \\[{alerts_count}\\]{first_alert_description}"
)

DAILY_FORECAST_UTC_HOUR: Final[int] = 4

# ? Add Default icon with ? mark
# ? Or Enum
ICON_ID_TO_EMOJI: Final[dict] = {
    "01d": "☀",
    "01n": "☀",
    "02d": "🌤",
    "02n": "☀",
    "03d": "☁️",
    "03n": "☁️",
    "04d": "☁️",
    "04n": "☁️",
    "09d": "🌦",
    "10d": "🌧",
    "11d": "⛈",
    "13d": "❄️",
    "50d": "🌫",
    "default": "🌤",
}
