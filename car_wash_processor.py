class CarWashDecisionProcessor:
    def __init__(self, lat, long, noaa_interface) -> None:
        self.lat = lat
        self.long = long
        self.noaa_interface = noaa_interface

    def get_weather_data(self):
        return self.noaa_interface.get_weather(self.lat, self.long)

    def do_wash(self):
        # Will return TRUE if it's a good day to wash car (more than 7 days before rain/snow)
        # Will return FALSE if it's not a good day to wash car 
        weather_data = self.get_weather_data()
        if sum(weather_data.values()) == 0:
            return True
        
        if all(x >= 7 for x in weather_data.values()):
            return True
        return False
