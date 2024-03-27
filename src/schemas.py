from mashumaro.mixins.orjson import DataClassORJSONMixin
from mashumaro import field_options
from dataclasses import field, dataclass

from src.telegram.helpers import escape_reserved_symbols


def deserialize_temperature(raw_temperature: float) -> str:
    """Convert temperature to int and escape reserved Telegram symbols."""
    temperature_repr = str(int(raw_temperature))

    return escape_reserved_symbols(temperature_repr)


@dataclass
class WeatherSummary(DataClassORJSONMixin):
    description: str
    icon_id: str = field(metadata=field_options(alias="icon"))


@dataclass
class DailyTemperatures(DataClassORJSONMixin):
    morning: str = field(
        metadata=field_options(alias="morn", deserialize=deserialize_temperature)
    )
    day: str = field(metadata=field_options(deserialize=deserialize_temperature))
    night: str = field(metadata=field_options(deserialize=deserialize_temperature))


@dataclass
class BaseWeather(DataClassORJSONMixin):
    uv_index: int = field(metadata=field_options(alias="uvi", deserialize=int))
    weather: list[WeatherSummary]


@dataclass
class CurrentWeather(BaseWeather, DataClassORJSONMixin):
    feels_like: str = field(metadata=field_options(deserialize=deserialize_temperature))
    actual_temperature: str = field(
        metadata=field_options(alias="temp", deserialize=deserialize_temperature)
    )


@dataclass
class DailyWeather(BaseWeather, DataClassORJSONMixin):
    feels_like: DailyTemperatures
    temp: DailyTemperatures
    summary: str


@dataclass
class Alert(DataClassORJSONMixin):
    event: str
    description: str
    start_time: int = field(metadata=field_options(alias="start"))
    end_time: int = field(metadata=field_options(alias="end"))


@dataclass
class OWMWeather(DataClassORJSONMixin):
    current: CurrentWeather
    daily: list[DailyWeather]
    alerts: list[Alert] = field(default_factory=lambda: [])
