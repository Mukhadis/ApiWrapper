from .Weather.weather import WeatherClient

def main():
    dublin = WeatherClient("Dublin")
    cork = WeatherClient("Cork")

    print(dublin.get_current_temperature())
    print(cork.get_current_temperature())

main()
