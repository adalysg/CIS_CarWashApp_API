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
    
    def weather_message(self, weather_data):
        # Precipitation ID = "PRCP"
        check_rain_or_snow = CheckRainOrSnow()
        check_rain_or_snow.yes_no_rain()
        check_rain_or_snow.yes_no_snow()