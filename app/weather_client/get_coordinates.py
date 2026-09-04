from __future__ import annotations
from ..constants import location_params, broken_coord_url, broken_weather_url
import requests


def get_latitude_and_longitude(url: str) -> tuple[float, float] | str:

    # Error handling for the API request. If the URL is wrong throw an error
    try:
        response = requests.get(url, params=location_params)
    except requests.exceptions.ConnectionError:
        return f"Could not reach '{url}'"

    # Error handling for a server side issue. If it is a 4XX or 5XX
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return f"ERROR: Could not reach the geocoding API [{response.status_code}]"

    # We manipulate the json data and extract the latitude and logitude we are looking for
    data = response.json()
    results = data["results"]
    relevant_info = results[0]
    latitude = relevant_info["latitude"]
    longitude = relevant_info["longitude"]
    coordinates = (latitude, longitude)
    return coordinates
