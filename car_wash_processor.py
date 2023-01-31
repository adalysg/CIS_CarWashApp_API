class CarWashDecisionProcessor:
    def __init__(self, lat, long, noaa_interface) -> None:
        self.lat = lat
        self.long = long
        self.noaa_interface = noaa_interface

    def get_weather_data(self):
        return self.noaa_interface.get_weather(self.lat, self.long)

    def do_wash(self, weather_data):
        # if statements?
        # Need to differentiate between rain or snow and return corresponding bool
        # (EX: if raining, but not snowing in state like FL, what do I return?)
        if weather_data['snow'] >= 10 and weather_data['rain'] >= 10:
            return True
        return False

    def wash_car_message(self):
        yes_wash_car_message = 'Today is a good day to wash your car.'
        no_do_not_wash_car_message = 'You should not was your car today.'
        if self.do_wash == True:
            print(no_do_not_wash_car_message)
        else:
            print(yes_wash_car_message)