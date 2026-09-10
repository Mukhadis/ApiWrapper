from __future__ import annotations
from .coordinates_client import get_latitude_and_longitude
from .temperature_client import get_temp

class WeatherClient:

    def get_current_temperature(self, city: str) -> str:
        try:
            coord = get_latitude_and_longitude(city)
            temp = get_temp(coord)
            return temp
        except KeyError:
            return f"'{city}' is an invalid input"
