# Name of file must start with "test"
# Test

import unittest
from unittest import TestCase
from unittest.mock import Mock
from car_wash_processor import CarWashDecisionProcessor
from check_rain_or_snow import CheckRainOrSnow

class TestCarWashDecisionProcessor(TestCase):
    def test_gets_weather_data_back(self):
        noaa_interface = Mock()
        car_wash_decision_processor = CarWashDecisionProcessor("fake_lat", "fake_long", noaa_interface)
        weather_data = car_wash_decision_processor.get_weather_data()
        noaa_interface.get_weather.assert_called_once_with("fake_lat", "fake_long")
        # Now that we have weather data, what do we do with it?

    # Through the next two tests, we now know that do_wash should take in weather_data in the 
    # format of a dict with certain keys and return a boolean depending on the keys' values
    def test_should_say_no_to_wash_car(self):
        car_wash_decision_processor = CarWashDecisionProcessor("fake_lat", "fake_long", Mock())
        weather_data = {"rain": 14, "snow": 10}
        res = car_wash_decision_processor.do_wash(weather_data)
        self.assertFalse(res)

    def test_should_say_yes_to_wash_car(self):
        car_wash_decision_processor = CarWashDecisionProcessor("fake_lat", "fake_long", Mock())
        weather_data = {"rain": 4, "snow": 1}
        res = car_wash_decision_processor.do_wash(weather_data)
        self.assertTrue(res)

    # Depending on boolean, we print a certain type of message
    def test_should_print_correct_no_message_depending_on_res_of_weather_data(self):
        car_wash_decision_processor = CarWashDecisionProcessor("fake_lat", "fake_long", Mock())
        weather_data = {"rain": 12, "snow": 10}
        res_no = car_wash_decision_processor.do_wash(weather_data)
        no_message = car_wash_decision_processor.wash_car_message(res_no)
        self.assertEqual(no_message, 'You should not was your car today.')

    def test_should_print_correct_yes_message_depending_on_res_of_weather_data(self):
        car_wash_decision_processor = CarWashDecisionProcessor("fake_lat", "fake_long", Mock())
        weather_data = {"rain": 4, "snow": 1}
        res_yes = car_wash_decision_processor.do_wash(weather_data)
        yes_message = car_wash_decision_processor.wash_car_message(res_yes)
        self.assertEqual(yes_message, 'Today is a good day to wash your car.')