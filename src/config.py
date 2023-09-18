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

# Pylance doesn't work well with BaseSettings
# https://docs.pydantic.dev/latest/visual_studio_code/#basesettings-and-ignoring-pylancepyright-errors
from pydantic import BaseSettings, Field, SecretStr

# from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    # model_config = SettingsConfigDict(case_sensitive=True)
    # bot_token: SecretStr
    bot_token: str = Field(str, alias="TELEGRAM_BOT_TOKEN")
    omp_api_key: str = Field(str, alias="OPENWEATHERMAP_API_KEY")
    # omp_api_key: SecretStr
    latitude: str
    longitude: str

    class Config:
        # case_sensitive = True
        env_file = ".env"
        # env_file_encoding = 'utf-8'


# OPENWEATHERMAP_REQUEST_TEMPLATE = (
#     "http://api.openweathermap.org/data/3.0/onecall?"
#     f"lat={Settings.latitude}&lon={Settings.longitude}&units=metric&exclude=minutely,hourly&"
#     f"appid={Settings.omp_api_key}"
# )
