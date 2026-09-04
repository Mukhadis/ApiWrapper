from .weather_client.get_coordinates import get_latitude_and_longitude
from .weather_client.get_weather import get_weather
from .constants import coord_url, weather_url


def main():
    coordinates = get_latitude_and_longitude(coord_url)
    weather = get_weather(coordinates, weather_url)
    print(weather)

main()
