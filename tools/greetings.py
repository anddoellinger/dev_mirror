import random
from tools import Times
from utils import greeting_summery


class Greetings:
    def __init__(self):
        self.today_greetings = []
        self.morning = 0
        self.afternoon = 1
        self.evening = 2
        self.night = 3
        self.times = Times()
        self.local_time = self.times.local_time()

    def greeting_choice(self):
        for i in range(4):
            self.today_greetings.append(random.choice(greeting_summery[i]))
        return self.today_greetings
