import pytest
from httpx import ConnectTimeout, HTTPStatusError
from pytest_httpx import HTTPXMock

from src.owm_api import fetch_weather, retrieve_weather_info
from tests.constants import OPENWEATHERMAP_REQUEST, OWM_RESPONSE_FRAGMENT


@pytest.mark.asyncio
async def test_retrieve_weather_info(
    httpx_mock: HTTPXMock, fake_owmweather, set_owm_api_env_variables
):
    httpx_mock.add_response(
        method="GET", url=OPENWEATHERMAP_REQUEST, text=OWM_RESPONSE_FRAGMENT
    )

    owmweather_instance = await retrieve_weather_info()

    assert owmweather_instance == fake_owmweather


@pytest.mark.asyncio
async def test_fetch_weather(httpx_mock: HTTPXMock, set_owm_api_env_variables):
    httpx_mock.add_response(method="GET", url=OPENWEATHERMAP_REQUEST, json={})

    json_response = await fetch_weather()

    assert json_response == {}


@pytest.mark.asyncio
async def test_fetch_weather__connection_timeout(
    httpx_mock: HTTPXMock, set_owm_api_env_variables
):
    httpx_mock.add_exception(ConnectTimeout(""), url=OPENWEATHERMAP_REQUEST)

    with pytest.raises(
        ConnectTimeout,
        match="Request to OpenWeatherMap API took more than 15.0 seconds",
    ):
        await fetch_weather()


@pytest.mark.asyncio
async def test_fetch_weather__unauthorized(
    httpx_mock: HTTPXMock, set_owm_api_env_variables
):
    httpx_mock.add_response(
        method="GET", url=OPENWEATHERMAP_REQUEST, json={}, status_code=401
    )

    with pytest.raises(HTTPStatusError):
        await fetch_weather()
