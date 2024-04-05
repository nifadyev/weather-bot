import pytest

from src.renderers import render_alerts, render_current_forecast
from src.schemas import Alert, OWMWeather


@pytest.mark.parametrize(
    argnames=("alerts", "expected_value"),
    argvalues=(
        (
            [
                Alert(
                    event="Other dangers",
                    description="Black ice",
                    start_time=1711522800,
                    end_time=1711598400,
                )
            ],
            ", black ice",
        ),
        (
            [Alert(event="Storm", description="", start_time=1234, end_time=98765)],
            "",
        ),
        ([], ""),
    ),
    ids=("full description", "empty description", "no alerts"),
)
def test_render_alerts(alerts: list[Alert], expected_value):
    assert render_alerts(alerts) == expected_value


def test_render_current_forecast(fake_owmweather: OWMWeather):
    expected_value = (
        "**Now feels like 5℃, Clear**\n\n"
        "**Weather forecast (next 24 hours)**\n"
        "☁️ Expect a day of partly cloudy with clear spells, black ice\n"
        "Morning: 0℃\n"
        "Day: 3℃\n"
        "Night: -1℃"
    )

    assert render_current_forecast(fake_owmweather) == expected_value
