from typing import Final

DEFAULT_TIMEOUT: Final[float] = 15.0

OPENWEATHERMAP_REQUEST_TEMPLATE: str = (
    "https://api.openweathermap.org/data/3.0/onecall?"
    "lat={latitude}&lon={longitude}&units=metric&exclude=minutely,hourly&appid={api_key}"
)
