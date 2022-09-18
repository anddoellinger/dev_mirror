from time import strftime
from utils import gmt_time_converter

# ---------------------------------
# Timezones in use
# ---------------------------------
# More timezones required???
# print(pytz.all_timezones_set)
# ---------------------------------


timezones = {'GER': 'Europe/Berlin', 'USA': 'America/New_York', 'MEX': 'America/Mexico_City', 'CHN': 'Asia/Shanghai'}

# ---------------------------------
# Current Timezone GMT Offset
# ---------------------------------
current_gmt_offset = gmt_time_converter(strftime('%z'))

# ---------------------------------
# Time & Date formats
# ---------------------------------
weekdays = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]

time_format = '%H:%M:%S'

# TODO Evening time should be equal to local sunset time
# TODO Maybe the daytimes are not necessary, daytime converter in times
# daytimes = ["08:55", "16:29", "18:30", "22:30"]

greeting_summery = (["Good Morning", "Have a nice Day", "Enjoy this Day", "Make the best out of this Day"],
                    ["Good Afternoon", "Enjoy the Afternoon", "Have a nice Afternoon"],
                    ["Good Evening", "Enjoy this evening", "First create, first execute"],
                    ["Good Night", "Sweet Dreams", "Restful Night"]
                    )

# ---------------------------------
# Locations
# More locations required???
# # Rapid API, locations can be found by name:
# # https://rapidapi.com/community/api/open-weather-map
# # Latitude and Longitude Finder, for more precise locations:
# # https://www.latlong.net/
# ---------------------------------

locations = {'KBC': {"q": "Kaltenbrunn,de", "lat": "50.1242", "lon": "10.8791", "cnt": "10", "units": "metric"},
             'PUE': {"q": "Puebla,MX", "lat": "19.045508", "lon": "-98.163755", "cnt": "10", "units": "metric"},
             'QRO': {"q": "Queretaro,MX", "lat": "20.689967", "lon": "-100.441752", "cnt": "10", "units": "metric"}
             }

# gmt_offset = weather.get_weather(locations['PUE'])['city']['timezone']
