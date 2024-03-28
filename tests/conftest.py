import os
import factory
from faker import Faker
import pytest

from telethon.events import NewMessage
from telethon.tl.patched import Message
from schemas import Alert, CurrentWeather, DailyTemperatures, DailyWeather, OWMWeather, WeatherSummary

fake = Faker()

class MessageFactory(factory.Factory):
    class Meta:
        model = Message

    id = 1
    peer_id = 2
    message: str = fake.text()

class EventFactory(factory.Factory):
    class Meta:
        model = NewMessage.Event

    message = factory.SubFactory(MessageFactory)

@pytest.fixture
def set_owm_api_env_variables():
    """Do not add scope to this fixture, it will break unit tests at test_owm_api.py."""
    os.environ["OPENWEATHERMAP_API_KEY"] = "fake_app_id"
    os.environ["LATITUDE"] = "12.3456789"
    os.environ["LONGITUDE"] = "98.7654321"

@pytest.fixture
def fake_owmweather() -> OWMWeather:
    current_weather = CurrentWeather(
        uv_index=0,
        weather=[WeatherSummary(description="Clear", icon_id="01d")],
        feels_like="5",
        actual_temperature="7",
    )
    daily_weather = DailyWeather(
        uv_index=1,
        weather=[WeatherSummary(description="Light rain", icon_id="04d")],
        feels_like=DailyTemperatures(morning="\\-2", day="2", night="\\-3"),
        temp=DailyTemperatures(morning="0", day="3", night="\\-1"),
        summary="Expect a day of partly cloudy with clear spells",
    )
    alert = Alert(
        event="Other dangers",
        description="Black ice",
        start_time=1711522800,
        end_time=1711598400,
    )
    return OWMWeather(
        current=current_weather, daily=[daily_weather], alerts=[alert]
    )
