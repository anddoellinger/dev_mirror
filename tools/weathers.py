from apis import WeathersAPI
import pytz
import datetime
from utils import unix_time_converter, speed_converter, timezones, customize_description
from tools import Times

weathers = WeathersAPI()
times = Times()


class Weathers:

    # Instance Variables
    def __init__(self):
        self.offset = pytz.timezone(timezones['MEX'])
        self.timezone_offset = datetime.datetime.now(self.offset)
        # !!!! The following value has to be changed when mirror is located in other timezone !!!!
        # GER = 0
        # USA = 1
        # MEX = 2
        self.local_offset = times.gtm_offsets()[2]
        # Function has to check if timezone data provided by api == to timezone_offset
        # if so no time must be added
        # else time offset (relative to GMT!)
        # TODO Get weather_dict back on the map including locations from Function call
        self.custom_icon = ''
        self.custom_description = ''

    def weather_info(self, location):
        weather_raw = weathers.get_weather(location)
        self.timezone_offset = weather_raw['timezone_offset']

        for value in times.gtm_offsets():
            if value == abs(self.timezone_offset):
                relative_offset = self.timezone_offset
                total_offset = relative_offset + self.local_offset
        # Min. Temp.
        min_temp = round(weather_raw['daily'][0]['temp']['min'])
        # Max. Temp.
        max_temp = round(weather_raw['daily'][0]['temp']['max'])
        # Feels like morning
        morning_feels = round(weather_raw['daily'][0]['feels_like']['day'])
        # Feels like evening
        evening_feels = round(weather_raw['daily'][0]['feels_like']['eve'])
        # Description
        description = customize_description(weather_raw['daily'][0]['weather'][0]['description'])[0]
        # Icon
        icon = customize_description(weather_raw['daily'][0]['weather'][0]['description'])[1]
        # Wind speed
        wind_speed_m_s = round(weather_raw['daily'][0]['wind_speed'], 1)
        wind_speed = round(speed_converter(wind_speed_m_s), 1)
        # Sunrise
        sunrise_data = str(unix_time_converter(weather_raw['daily'][0]['sunrise'] + total_offset))
        sunrise = sunrise_data[11:-3]
        # Sunset
        sunset_data = str(unix_time_converter(weather_raw['daily'][0]['sunset'] + total_offset))
        sunset = sunset_data[11:-3]
        return min_temp, max_temp, morning_feels, evening_feels, description, icon, wind_speed, sunrise, sunset
