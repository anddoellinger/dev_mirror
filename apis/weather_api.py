import requests
from utils import locations

# ********************** Sources **************************** #
# OpenWeatherMap API (documentation):
# https://openweathermap.org/api/one-call-3
# Latitude and Longitude Finder:
# https://www.latlong.net/


class WeathersAPI:
    # Class Variables
    locations = locations

    # Instance Variables
    def __init__(self):
        self.loc_code = ''
        self.main_url = 'https://api.openweathermap.org/data/3.0/onecall'
        self.units = 'metric'
        self.exclude = 'minutely,hourly'
        self.key = '39c7e12f89a58ee41eed38218327385a'

    def get_weather(self, location):
        """Function to get weather data form OpenWeatherMap API.
            Location data defined in utils/constants.py and used in tools/weathers."""
        lat = self.locations[location]['lat']
        lon = self.locations[location]['lon']
        url = f'{self.main_url}?lat={lat}&lon={lon}&units={self.units}&exclude={self.exclude}&appid={self.key}'
        result = requests.get(url)
        weather_raw = result.json()
        return weather_raw
