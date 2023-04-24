import httpx

from config import OPENWEATHERMAP_REQUEST_TEMPLATE


async def retrieve_weather_info() -> dict:
    raw_response = await fetch_weather()

    return parse_response(raw_response)


async def fetch_weather() -> dict:
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(OPENWEATHERMAP_REQUEST_TEMPLATE)

        return response.json()


def parse_response(raw_response: dict) -> dict:
    alerts_data = []
    if raw_alerts_data := raw_response.get("alerts"):
        alerts_data = [
            {
                "description": alert_data["description"],
                "event": alert_data["event"],
                "start_time": alert_data["start"],
                "end_time": alert_data["end"],
            }
            for alert_data in raw_alerts_data
        ]

    return {
        "now": {
            "feels_like": raw_response["current"]["feels_like"],
            "humidity": raw_response["current"]["humidity"],
            "actual_temperature": raw_response["current"]["temp"],
            "uv_index": raw_response["current"]["uvi"],
            "wind_speed": raw_response["current"]["wind_speed"],
            "wind_destination": raw_response["current"]["wind_deg"],
            "description": raw_response["current"]["weather"][0]["description"],
        },
        "today": {
            "description": raw_response["daily"][0]["weather"][0]["description"],
            "morning_feels_like": raw_response["daily"][0]["feels_like"]["morn"],
            "day_feels_like": raw_response["daily"][0]["feels_like"]["day"],
            "evening_feels_like": raw_response["daily"][0]["feels_like"]["eve"],
            "night_feels_like": raw_response["daily"][0]["feels_like"]["night"],
        },
        "alerts": alerts_data,
    }
