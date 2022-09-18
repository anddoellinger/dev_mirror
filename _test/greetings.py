import schedule
# import time
import random

morning_greeting_list = ["Good morning", "Have a nice day", "Enjoy this day", "Make the best out of this day"]
afternoon_greeting_list = ["Good afternoon", "Enjoy the afternoon", "Have a nice afternoon"]


def morning_greetings():
    display_greeting = random.choice(morning_greeting_list)
    print(display_greeting)


def afternoon_greetings():
    display_greeting = random.choice(afternoon_greeting_list)
    print(display_greeting)


while True:
    schedule.every().day.at("08:10:00").do(morning_greetings)
    schedule.every().day.at("12:00:00").do(afternoon_greetings)

