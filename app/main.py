from .Weather.weather import WeatherClient

weather = WeatherClient()
print(weather.get_current_temperature("Dublin"))
