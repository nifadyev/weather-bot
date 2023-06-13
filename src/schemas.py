from datetime import datetime

from pydantic import BaseModel, Field, confloat


class WeatherSummary(BaseModel):
    description: str
    icon_id: str = Field(str, alias="icon")


class DailyTemperatures(BaseModel):
    morning: int = Field(int, alias="morn")
    day: int
    night: int


class BaseWeather(BaseModel):
    clouds: int
    humidity: int
    uv_index: int = Field(int, alias="uvi")
    weather: list[WeatherSummary]
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
    start_time: datetime = Field(datetime, alias="start")
    end_time: datetime = Field(datetime, alias="end")


class OMPWeather(BaseModel):
    current: CurrentWeather
    daily: list[DailyWeather]
    alerts: list[Alert]
