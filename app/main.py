from .constants import city, coord_url, weather_url, location_params

import requests
import time


def get_latitude_and_longitude() -> tuple[str, str]:
    response = requests.get(coord_url, params=location_params)
    data = response.json()
    results = data["results"]
    relevant_info = results[0]
    latitude = relevant_info["latitude"]
    longitude = relevant_info["longitude"]
    coordinates = (latitude, longitude)
    return coordinates

def get_weather() -> str:
    coords = get_latitude_and_longitude()
    weather_params = {
        "latitude": coords[0],
        "longitude": coords[1],
        "hourly": "temperature_2m"
    }
    response = requests.get(weather_url, params=weather_params)
    data = response.json()
    hourly_weather = data["hourly"]
    current_hour = time.localtime().tm_hour
    weather_that_hour = hourly_weather["temperature_2m"]
    return f"Weather is currently {weather_that_hour[current_hour]}º celsius in {city}."

def main():
    print(get_weather())

main()
