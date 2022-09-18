import datetime


def lead_zero(number):
    if number < 10:
        leading_zero = "0" + str(number)
    else:
        leading_zero = "" + str(number)
    return leading_zero


def unix_time_converter(unix):
    converted_time = datetime.datetime.fromtimestamp(unix)
    return converted_time


def gmt_time_converter(row_time):
    extracted_time = int(row_time[-4:]) * 36
    return extracted_time


def speed_converter(input_speed):
    output_speed = input_speed * (1 / 3.6)
    return output_speed

# TODO no icon found, no description found does not work
def customize_description(default_description):
    if default_description == 'clear sky':
        custom_description = "Clear Sky"
        custom_icon = 'TBD'
    elif default_description == 'light rain':
        custom_description = "Light Rain"
        custom_icon = '10d-1'
    elif default_description == 'moderate rain':
        custom_description = "Moderate Rain"
        custom_icon = '10d-2'
    elif default_description == 'heavy rain':
        custom_description = "Heavy Rain"
        custom_icon = '10d-3'
    elif default_description == 'rain and snow':
        custom_description = "Sleet, Rain"
        custom_icon = '13d-1'
    elif default_description == 'light snow':
        custom_description = "Light Snow"
        custom_icon = '13d-1'
    elif default_description == 'scattered clouds':
        custom_description = "Scattered Clouds"
        custom_icon = '13d-1'
    elif default_description == 'few clouds':
        custom_description = "Few Clouds"
        custom_icon = '13d-1'
    elif default_description == 'broken clouds':
        custom_description = "Broken Clouds"
        custom_icon = '13d-1'
    elif default_description == 'overcast clouds':
        custom_description = "Overcast Clouds"
        custom_icon = 'TBD'
    else:
        custom_description = "Icon not found!!!"
        custom_icon = 'TBD'
    return custom_description, custom_icon
