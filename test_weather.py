from apis import WeathersAPI
from tools import Times
from tools import Weathers
from utils import locations
from utils import weekdays


weather = WeathersAPI()

print(weather.get_weather(locations['KBC']))

print(weather.get_weather(locations['KBC'])['city'])
print(weather.get_weather(locations['KBC'])["list"][0]["sunrise"])
# print(unix_time_converter(weather.get_weather(locations['KBC'])["list"][0]["sunrise"] +
#                           weather.get_weather(locations['KBC'])["city"]["timezone"]))
# print(unix_time_converter(weather.get_weather(locations['KBC'])["list"][0]["sunrise"]))
# print(weather.get_weather(locations['PUE'])['city'])
# print(weather.get_weather(locations['PUE'])["list"][0]["sunrise"])
# print(unix_time_converter(weather.get_weather(locations['PUE'])['list'][0]['sunrise'] +
#                           weather.get_weather(locations['PUE'])['city']['timezone']))
print(weather.get_weather(weather.get_weather(locations['PUE'])['list'][0]['sunrise']))
print(kb)

# print(weather.get_weather(locations['KBC'])["list"][0]["sunrise"])
# 'sunrise': 1648357459, 'sunset': 1648402758,
print(unix_time_converter(1648357459 + 21600 + 7200))
print(unix_time_converter(1648402758 + 21600 + 7200))
# + 7200 - 21600

print("Value: ")
print(unix_time_converter(176543))


# weather = Weathers()
# kaltenbrunn = weather.weather_info(locations['KBC'])
# print(kaltenbrunn)
weathers = Weathers()
QRO = weathers.weather_info(locations['QRO'])
# print("Weather in QRO")
# print("Max: " + QRO[0], QRO[1])
print(type(weathers.weather_info(locations['QRO'])))
print(weathers.weather_info(locations['QRO']))
print("Weather in PUE")
print(weathers.weather_info(locations['PUE']))
print("Weather in KBC")
print(weathers.weather_info(locations['KBC']))
times = Times()
daytime = times.local_daytime()
print(daytime)
# TODO Set the sunrise and sunset time related to GMTime offset below
print("Kaltenbrunn offset in h:")
print("Kaltenbrunn offset in sec:")
print("Offsets from Time for comprehension")
time_offset = times.gtm_offsets()
print(time_offset)
