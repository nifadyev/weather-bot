from datetime import datetime

from pydantic import BaseModel, Field, confloat


class WeatherSummary(BaseModel):
    # TODO: Parse \n in description
    description: str
    # TODO: Need mapping or enum
    icon_id: str = Field(str, alias="icon")

    # ? For all models
    class Config:
        allow_mutation = False


class DailyTemperatures(BaseModel):
    morning: int = Field(int, alias="morn")
    day: int
    night: int


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
    feels_like: int
    actual_temperature: int = Field(int, alias="temp")


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
