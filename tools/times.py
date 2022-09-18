import pytz
import datetime
# from tools import Greetings
from utils import time_format, timezones, gmt_time_converter, lead_zero, weekdays


class Times:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.current_time = self.now.strftime(time_format)
        self.datetime_ger = datetime.datetime.now(pytz.timezone(timezones['GER']))
        self.datetime_usa = datetime.datetime.now(pytz.timezone(timezones['USA']))
        self.datetime_mex = datetime.datetime.now(pytz.timezone(timezones['MEX']))
        self.datetime_chn = datetime.datetime.now(pytz.timezone(timezones['CHN']))
        self.today = datetime.date.today()
        self.year = self.today.year
        self.month = self.today.month
        self.day = self.today.day
        self.iso_week = self.today.isocalendar()
        self.morning = 0
        self.afternoon = 1
        self.evening = 2
        self.night = 3
        self.sunset_hour = 20

    def gtm_offsets(self):
        offset_ger = gmt_time_converter(self.datetime_ger.strftime('%z'))
        offset_usa = gmt_time_converter(self.datetime_usa.strftime('%z'))
        offset_mex = gmt_time_converter(self.datetime_mex.strftime('%z'))
        return offset_ger, offset_usa, offset_mex

    def timestamp(self):
        unix_time = datetime.datetime.timestamp(self.now)
        return unix_time

    def local_time(self):
        local_time = self.now.strftime(time_format)
        return local_time

    def hamburg_time(self):
        hamburg_time = self.datetime_ger.strftime(time_format)
        return hamburg_time

    def new_york_time(self):
        new_york_time = self.datetime_usa.strftime(time_format)
        return new_york_time

    def mexico_time(self):
        mexico_time = self.datetime_mex.strftime(time_format)
        return mexico_time

    def shanghai_time(self):
        shanghai_time = self.datetime_chn.strftime(time_format)
        return shanghai_time

    def local_date(self):
        local_date = f"{lead_zero(self.day)}.{lead_zero(self.month)}.{self.year}"
        return local_date

    def local_week(self):
        local_week = f"{lead_zero(self.iso_week[1])}/{str(self.year)[2:]}"
        return local_week

    def local_weekday(self):
        local_weekday = weekdays[self.iso_week[2] - 1]
        return local_weekday

    def local_daytime(self):
        result = 0
        local_h = int(self.local_time()[0:2])
        local_min = int(self.local_time()[3:5])
        sunset_hour = 19
        sunset_min = 19
        if local_h < 12:
            result = self.morning
        elif 12 <= local_h < self.sunset_hour or local_h == sunset_hour and local_min < sunset_min:
            result = self.afternoon
        elif local_h == sunset_hour and sunset_min <= local_min or local_h < 22 or local_h == 22 and local_min < 22:
            result = self.evening
        elif local_h == 22 and 22 <= local_min or 22 < local_h:
            result = self.night
        return result
