class CarWashDecisionProcessor:
    def __init__(self, lat, long, noaa_interface) -> None:
        self.lat = lat
        self.long = long
        self.noaa_interface = noaa_interface

    def get_weather_data(self):
        return self.noaa_interface.get_weather(self.lat, self.long)

    def do_wash(self, weather_data):
        # Will return TRUE if it's a good day to wash car (values <10)
        # Will return FALSE if it's not a good day to wash car (values >=10)
        if weather_data['snow'] < 10 and weather_data['rain'] < 10:
            return True
        return False

    def wash_car_message(self, do_wash_bool):
        yes_wash_car_message = 'Today is a good day to wash your car.'
        no_do_not_wash_car_message = 'You should not was your car today.'
        print(do_wash_bool)
        # do_wash returns True = you SHOULD wash car --> YES message 
        if do_wash_bool == True:
            return yes_wash_car_message
        # do_wash returns False = you should NOT wash car --> NO message
        else:
            return no_do_not_wash_car_message