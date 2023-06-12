# TODO: Use https://docs.pydantic.dev/usage/settings/#dotenv-env-support
from os import getenv

from dotenv import load_dotenv

load_dotenv()

# ? Does not set default values
TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN")
OPENWEATHERMAP_API_KEY = getenv("OPENWEATHERMAP_API_KEY")
BELGRADE_LATITUDE = "44.8178131"
BELGRADE_LONGITUDE = "20.4568974"
NN_LATITUDE = "56.3264816"
NN_LONGITUDE = "44.0051395"

# TODO: Later use string template and format
OPENWEATHERMAP_REQUEST_TEMPLATE = (
    "http://api.openweathermap.org/data/3.0/onecall?"
    f"lat={NN_LATITUDE}&lon={NN_LONGITUDE}&units=metric&exclude=minutely,hourly&"
    f"appid={OPENWEATHERMAP_API_KEY}"
)
