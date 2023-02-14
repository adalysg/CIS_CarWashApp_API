import os
import requests
import json
import re

class NoaaInterface():
    def __init__(self) -> None:
        self.client = requests

    def get_weather(self, lat, long):
        token = os.getenv("noaakey")
        weather_station = self.get_weather_station(lat, long, token)
        forecast = self.get_forecast(weather_station, token)
        # forecast = "delete this"
        return self.forecast_breakdown(forecast)

    # FUNCTION: Returns grid endpoint (url) for zone
    def get_weather_station(self, lat, long, token):
        res = self.client.get(f"https://api.weather.gov/points/{lat},{long}", headers={"token": token})
        print(res.text)
        forecast_url = json.loads(res.text)["properties"]["forecast"]
        return forecast_url

    # FUNCTION: Using the endpoint and token (permission), can generate json file with forecast 
    def get_forecast(self, forecast_url, token):
        res_forecast = self.client.get(forecast_url, headers={"token": token})
        return res_forecast

    def forecast_breakdown(self, forecast):
        periods = forecast['properties']['periods']
        rain_snow_forecast = {'rain': 0, 'snow': 0}

        # I don't like how there's two for loops --> is there a way to write with less lines of code?
        for value in periods:
            if re.search('[rR]ain|[pP]recipitation', value['detailedForecast']):
                rain_snow_forecast['rain'] = (int(value['number'])//2)
                break
        for value in periods:
            if re.search('[sS]now', value['detailedForecast']):
                rain_snow_forecast['snow'] = (int(value['number'])//2)
                break
        
        return rain_snow_forecast


