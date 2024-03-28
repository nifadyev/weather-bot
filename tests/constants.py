from typing import Final


OWM_RESPONSE_FRAGMENT: Final[str] = """
{
    "alerts": [
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
    ],
    "current": {
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
    },
    "daily": [
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
    ],
    "lat": 56.3265,
    "lon": 44.0051,
    "timezone": "Europe/Moscow",
    "timezone_offset": 10800
}
"""
