from fastapi import FastAPI
from clients.weather_client import WeatherClient
from clients.location_client import LocationClient

import sys
import os


app = FastAPI()
#TODO make secrets on my own
url = "save my secrets"
apiKey = "top secrets, i can't afford to be stolen"
weather = WeatherClient(url, apiKey)
locationInfo = LocationClient()


@app.get("/")
def root():
    return {"message": "My first FastAPI"}

@app.get("/home/{name}")
def hello(name: str):
    return {
        "message": f"Hello {name}"
    }

@app.get("/weather/home")
def weatherAtHome():
    location_data = locationInfo.getLocationInfo()
    if location_data:
        lat = location_data["latitude"]
        lon = location_data["longitude"]

        weather_json = weather.getCurrentConditions(lat,lon)
        if weather_json:
            temp = weather_json['temp']
            feels_like = weather_json['feels_like']
            return {
                "message": f"Hello, weather is {temp}. Feels like {feels_like}"
            }
    return {"message": "logic bug"}