from os import getenv
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN")
OPENWEATHERMAP_API_KEY = getenv("OPENWEATHERMAP_API_KEY")
LATITUDE = "44.8178131"
LONGITUDE = "20.4568974"

OPENWEATHERMAP_REQUEST_TEMPLATE = (
    "http://api.openweathermap.org/data/3.0/onecall?"
    f"lat={LATITUDE}&lon={LONGITUDE}&units=metric&exclude=minutely,hourly&"
    f"appid={OPENWEATHERMAP_API_KEY}"
)
