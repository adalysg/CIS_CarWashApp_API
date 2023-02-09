import os
import requests
import json

class NoaaInterface():
    def __init__(self) -> None:
        self.client = requests

    def get_weather(self, lat, long):
        token = os.getenv("noaakey")
        # weather_station = self.get_weather_station(lat, long, token)
        # forecast = self.get_forecast(weather_station, token)
        forecast = "delete this"
        return self.forecast_breakdown(forecast)

    def forecast_breakdown(self, forecast):
        # Needs to return dict with rain/snow key-values
        # RegEX to search for rain/precipitation and snow keywords --> check day # if matches found, 
        # floor divide by two --> if day is <= 7, return message
        

        return {'rain': 1, "snow": 0}
  
    def get_weather_station(self, lat, long, token):
        res = self.client.get(f"https://api.weather.gov/points/{lat},{long}", headers={"token": token})
        print(res.text)
        forecast_url = json.loads(res.text)["properties"]["forecast"]
        return forecast_url

    def get_forecast(self, forecast_url, token):
        res_forecast = self.client.get(forecast_url, headers={"token": token})
        return res_forecast

