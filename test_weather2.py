from tools import Weathers


weathers = Weathers()
weather_first = weathers.weather_info('QRO')
weather_second = weathers.weather_info('KBC')
weather_third = weathers.weather_info('PUE')

print(weather_first)
print(weather_second)
print(weather_third)
print(weather_third[4])
print(weather_second[6])
print(type(weather_second[6]))
