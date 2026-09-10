from __future__ import annotations
from .constants import weather_url
import requests
import time

def get_temp(coordinates: tuple[tuple[float, float], str] | str) -> str | float:

    city = coordinates[1]
    url = weather_url

    if type(coordinates) == str:
        return coordinates
    else:
        # These are the parameters we are going to feed into the request as parameters if coordiates is indeed a Tuple type
        temp_params = {
            "latitude": coordinates[0][0],
            "longitude": coordinates[0][1],
            "hourly": "temperature_2m"
        }

    # Same logic as prior. If the URL does not exist handle
    try:
        response = requests.get(url, params=temp_params)
    except requests.exceptions.ConnectionError:
        return f"Could not reach '{url}'"

    # Error handling for a server side issue. If it is a 4XX or 5XX
    try:
        # We manipulate the data here to extract only the temperature for a particular hour in the day. If there is a KeyError we
        response.raise_for_status()
        data = response.json()
        hourly_temp = data["hourly"]
        current_hour = time.localtime().tm_hour
        temp_that_hour = hourly_temp["temperature_2m"]
        return temp_that_hour[current_hour]
    except requests.exceptions.HTTPError:
        return f"ERROR: Could not reach the temp API [{response.status_code}]"
