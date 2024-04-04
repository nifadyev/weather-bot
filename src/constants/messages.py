from typing import Final

START_MESSAGE: Final[str] = """
👋 Hi, this is Weather bot

I provide actual (so called "feels" like") weather forecast by request or by periodic messages. You can customize schedule and location.

I am in beta so please do not expect seamless and bug-free experience
"""

CURRENT_FORECAST_TEMPLATE_EN: str = (
    "**Now feels like {current_temperature}℃, {current_summary}**\n\n"
    "**Weather forecast (next 24 hours)**\n"
    "{icon} {summary}{alert}\n"
    "Morning: {morning_temperature}℃\n"
    "Day: {day_temperature}℃\n"
    "Night: {night_temperature}℃"
)

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
