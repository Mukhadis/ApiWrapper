from .Weather.weather import WeatherClient

def main():
    weather = WeatherClient()
    print(weather.get_current_temperature("Dublin"))

main()
