import unittest
from unittest import TestCase
from unittest.mock import Mock, patch
from car_wash_processor import CarWashDecisionProcessor
from noaa_interface import NoaaInterface
import json

# Are we calling NOAA they way it should be called?
class TestCarWashDecisionProcessorIntegration(TestCase):

    # specified object (get_forecast & get_weather_station of the NoaaInterface class) will be 
    # replaced with a mock during test and is restored afterwards
    @patch.object(NoaaInterface, 'get_forecast')
    @patch.object(NoaaInterface, 'get_weather_station')
    def test_gets_weather_data_back(self, mock_weather_station, mock_forecast):
        # noaa_repsonse = fixed
        with open('noaa_response.json', 'r+') as f:
            fake_forecast = json.load(f)            
        fake_weather_station = "fake_url.com"
        mock_weather_station.return_value = fake_weather_station
        mock_forecast.return_value = fake_forecast
        noaa_interface = NoaaInterface()
        car_wash_decision_processor = CarWashDecisionProcessor("28.6610945","-81.4606445", noaa_interface)
        weather_data = car_wash_decision_processor.get_weather_data()
        # "rain" keyword in "number": 3 (3//2=1) and "snow" keyword in "number": 7 (7//2=3)
        self.assertEqual(weather_data, {'rain': 1, 'snow': 3}) 

class TestCarWashDecisionProcessorIntegration2(TestCase):

    @patch.object(NoaaInterface, 'get_forecast')
    @patch.object(NoaaInterface, 'get_weather_station')
    def test_gets_weather_data_back(self, mock_weather_station, mock_forecast):
        with open('noaa_response_2.json', 'r+') as f:
            fake_forecast = json.load(f)            
        fake_weather_station = "fake_url.com"
        mock_weather_station.return_value = fake_weather_station
        mock_forecast.return_value = fake_forecast
        noaa_interface = NoaaInterface()
        car_wash_decision_processor = CarWashDecisionProcessor("28.6610945","-81.4606445", noaa_interface)
        weather_data = car_wash_decision_processor.get_weather_data()
        self.assertEqual(weather_data, {'rain': 0, 'snow': 0}) 
