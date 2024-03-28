from os import getenv

from httpx import AsyncClient, ConnectTimeout
from dotenv import load_dotenv

from constants.owm_api import DEFAULT_TIMEOUT, OPENWEATHERMAP_REQUEST_TEMPLATE
from schemas import OWMWeather

load_dotenv()


async def retrieve_weather_info() -> OWMWeather:
    raw_response = await fetch_weather()

    return validate_response(raw_response)


async def fetch_weather() -> dict:
    api_request = render_api_request()

    async with AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
        try:
            response = await client.get(api_request)
        except ConnectTimeout:
            raise ConnectTimeout(
                message=f"Request to OpenWeatherMap API took more than {DEFAULT_TIMEOUT} seconds",
            )

        response.raise_for_status()

        return response.json()


def render_api_request() -> str:
    if not (api_key := getenv("OPENWEATHERMAP_API_KEY")):
        raise ValueError("Env variable `OPENWEATHERMAP_API_KEY` is missing or empty")
    if not (latitude := getenv("LATITUDE")):
        raise ValueError("Env variable `LATITUDE` is missing or empty")
    if not (longitude := getenv("LONGITUDE")):
        raise ValueError("Env variable `LONGITUDE` is missing or empty")

    return OPENWEATHERMAP_REQUEST_TEMPLATE.format(
        api_key=api_key, latitude=latitude, longitude=longitude
    )


def validate_response(raw_response: dict) -> OWMWeather:
    return OWMWeather.from_dict(raw_response)
