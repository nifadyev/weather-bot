import httpx

from config import OPENWEATHERMAP_REQUEST_TEMPLATE
from schemas import OMPWeather


async def retrieve_weather_info() -> OMPWeather:
    raw_response = await fetch_weather()

    return validate_response(raw_response)


async def fetch_weather() -> dict:
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(OPENWEATHERMAP_REQUEST_TEMPLATE)

        return response.json()


def validate_response(raw_response: dict) -> OMPWeather:
    return OMPWeather(**raw_response)
