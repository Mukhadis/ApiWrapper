from .Weather.weather import Weather

def main():
    weather = Weather()
    print(weather.get_current_temperature("Paris"))

main()
