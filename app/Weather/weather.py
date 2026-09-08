from __future__ import annotations
from .coordinates_client import get_latitude_and_longitude
from .temperature_client import get_temp

class WeatherClient:
    def __init__(self, city: str) -> None:
        self.city = city

    def get_current_temperature(self) -> str:
        try:
            coord = get_latitude_and_longitude(self.city)
            temp = get_temp(coord)
            return temp
        except KeyError:
            return f"'{self.city}' is an invalid input"
