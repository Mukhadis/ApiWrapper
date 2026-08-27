import requests
import time

city = "Dublin"
coord_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"

def get_latitude_and_longitude(coord_url: str) -> tuple[str, str]:
    response = requests.get(coord_url)
    data = response.json()
    results = data["results"]
    relevant_info = results[0]
    latitude = relevant_info["latitude"]
    longitude = relevant_info["longitude"]
    coordinates = (latitude, longitude)
    return coordinates

def get_weather() -> str:
    coordinates = get_latitude_and_longitude(coord_url)
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={coordinates[0]}&longitude={coordinates[1]}&hourly=temperature_2m&forecast_days=1")
    data = response.json()
    hourly_weather = data["hourly"]
    current_hour = time.localtime().tm_hour
    weather_that_hour = hourly_weather["temperature_2m"]
    return f"Weather is currently {weather_that_hour[current_hour]}º celsius in {city}."

def main():
    print(get_weather())

main()
