from datetime import date
# ---------------------------------------------
from utils import lead_zero, weekdays


class Dates:
    def __init__(self):
        self.today = date.today()
        self.year = self.today.year
        self.month = self.today.month
        self.day = self.today.day
        self.iso_week = self.today.isocalendar()

    def get_date(self):
        current_date = f"{lead_zero(self.day)}.{lead_zero(self.month)}.{self.year}"
        return current_date

    def get_week(self):
        current_week = f"{lead_zero(self.iso_week[1])}/{str(self.year)[2:]}"
        return current_week

    def get_weekday(self):
        weekday = weekdays[self.iso_week[2] - 1]
        return weekday


# current_iso_week = self.today.isocalendar()
# current_week = f"{lead_zero(current_iso_week[1])}/{str(current_year)[2:]}"
# , current_week


# def dates():
#     while True:
#         today = date.today()
#         current_year = today.year
#         current_iso_week = today.isocalendar()
#         current_date = f"{lead_zero(today.day)}.{lead_zero(today.month)}.{today.year}"
#         current_week = f"{lead_zero(current_iso_week[1])}/{str(current_year)[2:]}"
#         return current_date, current_week
#
#
#
# print(dates())
