class CarWashDecisionProcessor:
    def __init__(self, lat, long, noaa_interface) -> None:
        self.lat = lat
        self.long = long
        self.noaa_interface = noaa_interface

    def get_weather_data(self):
        return self.noaa_interface.get_weather(self.lat, self.long)

