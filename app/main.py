from __future__ import annotations

from .constants import city, coord_url, weather_url, location_params, break_test_url
from typing import Any

import requests
import time

def get_latitude_and_longitude() -> tuple[int, int] | str:
    try:
        response = requests.get(coord_url, params=location_params)
        data = response.json()
        results = data["results"]
        relevant_info = results[0]
        latitude = relevant_info["latitude"]
        longitude = relevant_info["longitude"]
        coordinates = (latitude, longitude)
        return coordinates
    except requests.exceptions.ConnectionError:
        return "Error: Could not reach the geocoding API"

def get_weather(coordinates: tuple[int, int] | str) -> tuple[int, int] | str:
    weather_params = {
        "latitude": coordinates[0],
        "longitude": coordinates[1],
        "hourly": "temperature_2m"
    }
    try:
        response = requests.get(weather_url, params=weather_params)
        data = response.json()
        hourly_weather = data["hourly"]
        current_hour = time.localtime().tm_hour
        weather_that_hour = hourly_weather["temperature_2m"]
        return f"Weather is currently {weather_that_hour[current_hour]}º celsius in {city}."
    except requests.exceptions.ConnectionError:
        return f"Could not reach the weather API"
    except KeyError:
        return coordinates

def main():
    print(get_weather(get_latitude_and_longitude()))

main()
