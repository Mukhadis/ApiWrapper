from __future__ import annotations

from .constants import city, coord_url, weather_url, location_params, break_test_url
from typing import Any

import requests
import time

def get_latitude_and_longitude() -> tuple[int, int] | str:

    # Error handling for the API request. If we cannot reach the geocoding API we handle it gracefully
    try:
        response = requests.get(coord_url, params=location_params)
    except requests.exceptions.ConnectionError:
        return f"Error: Could not reach the geocoding API"

    # We manipulate the json data and extract the latitude and logitude we are looking for
    data = response.json()
    results = data["results"]
    relevant_info = results[0]
    latitude = relevant_info["latitude"]
    longitude = relevant_info["longitude"]
    coordinates = (latitude, longitude)
    return coordinates

def get_weather(coordinates: tuple[int, int] | str) -> tuple[int, int] | str:

    # These are the parameters we are going to feed into the request as parameters
    weather_params = {
        "latitude": coordinates[0],
        "longitude": coordinates[1],
        "hourly": "temperature_2m"
    }

    # Same logic as prior. If we cannot reach the Weather API. Handle the error gracefully
    try:
        response = requests.get(weather_url, params=weather_params)
    except requests.exceptions.ConnectionError:
        return f"Could not reach the weather API"

    # We manipulate the data here to extract only the temperature for a particular hour in the day. If there is a KeyError we
    # flag that as the previous API request failing and return the error we made for it
    try:
        data = response.json()
        hourly_weather = data["hourly"]
        current_hour = time.localtime().tm_hour
        weather_that_hour = hourly_weather["temperature_2m"]
        return f"Weather is currently {weather_that_hour[current_hour]}º celsius in {city}."
    except KeyError:
        return coordinates

def main():
    print(get_weather(get_latitude_and_longitude()))

main()
