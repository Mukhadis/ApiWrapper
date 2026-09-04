from __future__ import annotations
from ..constants import city
import requests
import time

def get_weather(coordinates: tuple[int, int] | str, url: str) -> tuple[int, int] | str:

    # These are the parameters we are going to feed into the request as parameters
    weather_params = {
        "latitude": coordinates[0],
        "longitude": coordinates[1],
        "hourly": "temperature_2m"
    }

    # Same logic as prior. If the URL does not exist handle
    try:
        response = requests.get(url, params=weather_params)
    except requests.exceptions.ConnectionError:
        return f"Could not reach '{url}'"

    # Error handling for a server side issue. If it is a 4XX or 5XX
    try:
        # We manipulate the data here to extract only the temperature for a particular hour in the day. If there is a KeyError we
        response.raise_for_status()
        data = response.json()
        hourly_weather = data["hourly"]
        current_hour = time.localtime().tm_hour
        weather_that_hour = hourly_weather["temperature_2m"]
        return f"Weather is currently {weather_that_hour[current_hour]}º celsius in {city}."
    except requests.exceptions.HTTPError:
        if response.status_code == 400:
            return coordinates
        else:
            return f"ERROR: Could not reach the weather API [{response.status_code}]"
