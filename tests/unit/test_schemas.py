import pytest

from src.schemas import Alert, BaseWeather, WeatherSummary


def test_weather_summary():
    raw_json = '{"description": "clear", "icon": "01d", "id": 800, "main": "Clear"}'
    expected_schema = WeatherSummary(description="clear", icon_id="01d")

    assert WeatherSummary.from_json(raw_json) == expected_schema


def test_base_weather():
    raw_json = """
    {
        "uvi": 3,
        "weather": [{"description": "Cloudy", "icon": "04d", "id": 804, "main": "Clouds"}]
    }
    """
    expected_schema = BaseWeather(
        uv_index=3, weather=[WeatherSummary(description="Cloudy", icon_id="04d")]
    )

    assert BaseWeather.from_json(raw_json) == expected_schema


def test_alert():
    raw_json = """
    {
        "description": "Black ice",
        "end": 1711598400,
        "event": "Other dangers",
        "sender_name": "web@mecom.ru",
        "start": 1711522800,
        "tags": [
            "Other dangers"
        ]
    }
    """
    expected_schema = Alert(
        event="Other dangers",
        description="Black ice",
        start_time=1711522800,
        end_time=1711598400,
    )

    assert Alert.from_json(raw_json) == expected_schema


def test_alert_value_type_is_changed():
    """Raise standard `mashumaro` error if field type has been changed."""
    raw_json = """
    {
        "description": "Black ice",
        "end": "Mar 11th, 2024",
        "event": "Other dangers",
        "sender_name": "web@mecom.ru",
        "start": "Mar 10th, 2024",
        "tags": [
            "Other dangers"
        ]
    }
    """

    with pytest.raises(ValueError):
        Alert.from_json(raw_json)
