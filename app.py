from flask import Flask, render_template, jsonify
from tools import Times, Greetings, Weathers
from utils import locations

# TODO instance not necessary??
app = Flask(__name__, instance_relative_config=True)

# TODO SEND_FILE seems not to be necessary
app.config.update(
    DEBUG=True,
    # SEND_FILE_MAX_AGE_DEFAULT=0
)

# Tools to call at app startup
greetings = Greetings()
greetings_choice = greetings.greeting_choice()

weathers = Weathers()
weather_first = weathers.weather_info('QRO')
weather_second = weathers.weather_info('KBC')
weather_third = weathers.weather_info('PUE')


# Tools to call on specific time
# TODO Can times be called here instead as part of Function refresh()??

@app.route('/refresh-tool', methods=['GET'])
def refresh():
    times = Times()

    # Triggering tasks on specific time
    # if times.local_time() == "05:30:00":
    #     # Call weather app to reload data
    #
    #     KBC = weathers.weather_info(locations['KBC'])
    #     PUE = weathers.weather_info(locations['PUE'])
    #
    # elif times.local_time() == "11:11:00":
    #     # Call weather app to reload data for the rest of the day
    #     print("triggered again")

    # TODO Comprehension between current daytime (Times) and constants time just work in the specific hour e.g. 16:00
    #  until 16:59. Check comprehension in tools/greetings
    # TODO QRO should not be a global parameter, is the parameter working?
    return jsonify(local=times.local_time(), hamburg=times.hamburg_time(), new_york=times.new_york_time(),
                   shanghai=times.shanghai_time(), date=times.local_date(), week=times.local_week(),
                   weekday=times.local_weekday(),
                   # ***** Weather Data *****
                   first_temp_min=weather_first[0], first_temp_max=weather_first[1],
                   first_feels_morning=weather_first[2], first_feels_evening=weather_first[3],
                   first_temp_descript=weather_first[4], first_wind_speed=weather_first[6],
                   first_sunrise=weather_first[7], first_sunset=weather_first[8],
                   second_temp_min=13, second_temp_max=26, second_feels_mor=25, second_feels_eve=23,
                   second_temp_desc='Few Clouds', second_wind_speed=2.2, second_sunrise='07:18', second_sunset='20:17',
                   third_temp_min=13, third_temp_max=26, thierd_feels_mor=25, thierd_feels_eve=23,
                   third_temp_desc='Few Clouds', thierd_wind_speed=2.2, thierd_sunrise='07:18', thierd_sunset='20:17'
                   )


@app.route('/')
def time_refresh():
    return render_template('index.html')


# @app.route('/mirror')
# def mirror():
#     return render_template('mirror.html')


# TODO Check if reloader is necessary
if __name__ == "__main__":
    app.run(use_reloader=True)
    # server = Server(app.wsgi_app)
    # server.watch('templates/', delay=0.5)
    # server.serve(port=8080, host='localhost')
# use_debugger=True,

# ****************SOURCES****************
# Reload
# https://gist.github.com/lost-theory/4521102
