# Name of file must start with "test"
# Test

import unittest
from unittest import TestCase
from unittest.mock import Mock
from car_wash_processor import CarWashDecisionProcessor

class TestCarWashDecisionProcessor(TestCase):
    def test_gets_weather_data_back(self):
        noaa_interface = Mock()
        car_wash_decision_processor = CarWashDecisionProcessor("fake_lat", "fake_long", noaa_interface)
        weather_data = car_wash_decision_processor.get_weather_data()
        noaa_interface.get_weather.assert_called_once_with("fake_lat", "fake_long")
        # Now that we have weather data, what do we do with it?

    def test_returns_true_if_all_weather_equals_7(self):
        noaa_mock = Mock()
        noaa_mock.get_weather.return_value = {'rain': 7, 'snow': 7}
        car_wash_decision_processor = CarWashDecisionProcessor("fake_lat", "fake_long", noaa_mock)
        do_wash_bool = car_wash_decision_processor.do_wash()
        self.assertTrue(do_wash_bool)

    def test_returns_false_if_any_weather_less_than_7(self):
        noaa_mock = Mock()
        noaa_mock.get_weather.return_value = {'rain': 4, 'snow': 7}
        car_wash_decision_processor = CarWashDecisionProcessor("fake_lat", "fake_long", noaa_mock)
        do_wash_bool = car_wash_decision_processor.do_wash()
        self.assertFalse(do_wash_bool)

    def test_returns_true_if_all_weather_exceeds_current_week(self):
        noaa_mock = Mock()
        noaa_mock.get_weather.return_value = {'rain': 0, 'snow': 0}
        car_wash_decision_processor = CarWashDecisionProcessor("fake_lat", "fake_long", noaa_mock)
        do_wash_bool = car_wash_decision_processor.do_wash()
        self.assertTrue(do_wash_bool)