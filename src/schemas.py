from datetime import datetime

from pydantic import BaseModel, Field, confloat, validator
from telegram.helpers import escape_markdown


def escape_special_symbols(float_repr_temperature: str) -> str:
    """Drop floating part from temperature repr and escape reserved Telegram symbols.

    For example, symbol `-` should be escaped.
    """
    if len(float_repr_temperature) == 1:
        int_repr_temperature = float_repr_temperature
    else:
        int_repr_temperature = float_repr_temperature[:-3]

    return escape_markdown(text=int_repr_temperature, version=2)


class WeatherSummary(BaseModel):
    # TODO: Parse \n in description
    description: str
    # TODO: Need mapping or enum
    icon_id: str = Field(str, alias="icon")

    # ? For all models
    class Config:
        allow_mutation = False


class DailyTemperatures(BaseModel):
    morning: str = Field(default=..., alias="morn")
    day: str = Field(default=...)
    night: str = Field(default=...)

    _escape_special_symbols_morning = validator("morning", allow_reuse=True)(escape_special_symbols)
    _escape_special_symbols_day = validator("day", allow_reuse=True)(escape_special_symbols)
    _escape_special_symbols_night = validator("night", allow_reuse=True)(escape_special_symbols)


class BaseWeather(BaseModel):
    # ? Transform to str based on value
    clouds: int
    humidity: int
    uv_index: int = Field(int, alias="uvi")
    # ? conlist(WeatherSummary, min_items=1, max_items=1) list with only 1 item
    weather: list[WeatherSummary]
    # TODO: convert to str like north, east-south, etc
    # In degrees, need to convert to south/north, etc based on it
    # Or just add warning if strong wind with bad destination
    # ? or conint(0, 360)
    # ? expect str and in validator convert to int and check ranges
    wind_direction: int = Field(int, alias="wind_deg")
    wind_speed: int


class CurrentWeather(BaseWeather):
    feels_like: str = Field(default=...)
    actual_temperature: str = Field(default=..., alias="temp")

    _escape_special_symbols_feels_like = validator("feels_like", allow_reuse=True)(
        escape_special_symbols
    )
    _escape_special_symbols_actual_temperature = validator("actual_temperature", allow_reuse=True)(
        escape_special_symbols
    )


class DailyWeather(BaseWeather):
    feels_like: DailyTemperatures
    temp: DailyTemperatures
    summary: str
    # pop from daily - Probability of precipitation
    pop: confloat(ge=0, le=1)


class Alert(BaseModel):
    event: str
    description: str
    # TODO: check offset from UTC
    # ? Or just make field duration (smth like repr in Django)
    start_time: datetime = Field(datetime, alias="start")
    end_time: datetime = Field(datetime, alias="end")


class OMPWeather(BaseModel):
    current: CurrentWeather
    daily: list[DailyWeather]
    alerts: list[Alert] = []
