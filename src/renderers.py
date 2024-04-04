from constants.messages import CURRENT_FORECAST_TEMPLATE_EN, ICON_ID_TO_EMOJI
from schemas import Alert, OWMWeather


def render_alerts(alerts: list[Alert]) -> str:
    """Usually, only first item is localized."""
    if alerts and (alert_description := alerts[0].description):
        return f", {alert_description.lower()}"

    return ""

def render_current_forecast(forecast: OWMWeather) -> str:
    today_forecast = forecast.daily[0]

    return CURRENT_FORECAST_TEMPLATE_EN.format(
        icon=ICON_ID_TO_EMOJI.get(
            today_forecast.weather[0].icon_id, ICON_ID_TO_EMOJI["default"]
        ),
        summary=today_forecast.summary,
        current_temperature=forecast.current.feels_like,
        current_summary=forecast.current.weather[0].description,
        morning_temperature=today_forecast.temp.morning,
        day_temperature=today_forecast.temp.day,
        night_temperature=today_forecast.temp.night,
        alert=render_alerts(forecast.alerts),
    )
