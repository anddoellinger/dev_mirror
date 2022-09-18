from utils import locations, unix_time_converter
from tools import Times, Weathers

times = Times()
weathers = Weathers()
print((type(times.local_time())), times.local_time())
if times.local_time == "05:30:00" or times.local_time == "10:15:00":
    QRO = weathers.weather_info(locations['QRO'])
    KBC = weathers.weather_info(locations['KBC'])
    PUE = weathers.weather_info(locations['PUE'])


# times.local_time()

unix_test = unix_time_converter(1659870000)
print(unix_test)
