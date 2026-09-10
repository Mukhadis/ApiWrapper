from .Weather.weather import WeatherClient
from fastapi import FastAPI

input = "Dublin"

client = WeatherClient()
temp = client.get_current_temperature(input)

app = FastAPI()

@app.get(f"/weather/{input}")
def get_temp():
    return {
        "city": input,
        "temp": temp
    }
