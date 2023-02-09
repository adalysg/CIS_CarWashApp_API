class CarWashDecisionProcessor:
    def __init__(self, lat, long, noaa_interface) -> None:
        self.lat = lat
        self.long = long
        self.noaa_interface = noaa_interface

    def get_weather_data(self):
        return self.noaa_interface.get_weather(self.lat, self.long)

    def do_wash(self):
        # Will return TRUE if it's a good day to wash car (values <10)
        # Will return FALSE if it's not a good day to wash car (values >=10)
        weather_data = self.get_weather_data()
        if weather_data['snow'] >= 7 and weather_data['rain'] >= 7:
            return True
        return False
        