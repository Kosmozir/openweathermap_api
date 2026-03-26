from dataclasses import dataclass

@dataclass
class Locaation:
    zip: str
    name: str
    lat: str
    lon: str
    country: str

@dataclass
class WeatherData:
    coord: dict
    weather: list
    base: str
    main: dict
    visibility: int
    wind: dict
    clouds: dict
    dt: int
    sys: dict
    timezone: int
    id: int
    name: str
    cod: int

