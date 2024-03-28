from src.schemas import (
    Alert,
    CurrentWeather,
    DailyTemperatures,
    DailyWeather,
    OWMWeather,
    WeatherSummary,
)
from tests.constants import OWM_RESPONSE_FRAGMENT

def test_daily_temperatures():
    raw_json = '{"day": 6.35, "eve": 1.04, "morn": -0.13, "night": -2.47}'
    expected_schema = DailyTemperatures(morning="0", day="6", night="\\-2")

    assert DailyTemperatures.from_json(raw_json) == expected_schema


def test_current_weather():
    raw_json = """
    {
        "clouds": "0",
        "dew_point": -6.46,
        "dt": 1711022278,
        "feels_like": 5.59,
        "humidity": 34,
        "pressure": 1024,
        "sunrise": 1710990175,
        "sunset": 1711034353,
        "temp": 7.57,
        "uvi": 0.61,
        "visibility": 10000,
        "weather": [{"description": "Clear", "icon": "01d", "id": 800, "main": "Clear"}],
        "wind_deg": 230,
        "wind_speed": 3
    }
    """
    expected_schema = CurrentWeather(
        uv_index=0,
        weather=[WeatherSummary(description="Clear", icon_id="01d")],
        feels_like="5",
        actual_temperature="7",
    )

    assert CurrentWeather.from_json(raw_json) == expected_schema


def test_daily_weather():
    raw_json = """
    {
        "clouds": 60,
        "dew_point": -0.58,
        "dt": 1711011600,
        "feels_like": {"day": 2.31, "eve": 1.04, "morn": -2.25, "night": -3.5},
        "humidity": 73,
        "moon_phase": 0.38,
        "moonrise": 1711017360,
        "moonset": 1710988860,
        "pop": 0,
        "pressure": 1026,
        "summary": "Expect a day of partly cloudy with clear spells",
        "sunrise": 1710990175,
        "sunset": 1711034353,
        "temp": {
            "day": 3.73,
            "eve": 3.45,
            "max": 7.57,
            "min": -0.54,
            "morn": -0.38,
            "night": -1.42
        },
        "uvi": 1.32,
        "weather": [
            {
                "description": "Light rain",
                "icon": "04d",
                "id": 803,
                "main": "Clouds"
            }
        ],
        "wind_deg": 254,
        "wind_gust": 4.76,
        "wind_speed": 2.86
    }
    """
    expected_schema = DailyWeather(
        uv_index=1,
        weather=[WeatherSummary(description="Light rain", icon_id="04d")],
        feels_like=DailyTemperatures(morning="\\-2", day="2", night="\\-3"),
        temp=DailyTemperatures(morning="0", day="3", night="\\-1"),
        summary="Expect a day of partly cloudy with clear spells",
    )

    assert DailyWeather.from_json(raw_json) == expected_schema


# For some reason fake_owmweather is not equal to expected_schema
def test_owmweather():
    """Create `OWMWeather` dataclass from actual API response fragment."""
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
    expected_schema = OWMWeather(
        current=current_weather, daily=[daily_weather], alerts=[alert]
    )

    assert OWMWeather.from_json(OWM_RESPONSE_FRAGMENT) == expected_schema


def test_owmweather_default_alerts():
    """Handle shortened API response fragment without field `alerts`."""
    raw_json = """
    {
        "current": {
            "clouds": "0",
            "feels_like": 5.59,
            "temp": 7.57,
            "uvi": 0.61,
            "weather": [{"description": "Clear", "icon": "01d", "id": 800, "main": "Clear"}]
        },
        "daily": [
            {
                "feels_like": {"day": 2.31, "eve": 1.04, "morn": -2.25, "night": -3.5},
                "summary": "Expect a day of partly cloudy with clear spells",
                "temp": {
                    "day": 3.73,
                    "morn": -0.38,
                    "night": -1.42
                },
                "uvi": 1.32,
                "weather": [{"description": "Light rain", "icon": "04d"}]
            }
        ]
    }
    """
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
    expected_schema = OWMWeather(current=current_weather, daily=[daily_weather])

    assert OWMWeather.from_json(raw_json) == expected_schema
