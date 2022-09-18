from O365 import Account, FileSystemTokenBackend, MSGraphProtocol
import time
from datetime import datetime, timedelta

# ********************** Sources **************************** #
# O365 Tutorial:
# https://pietrowicz-eric.medium.com/how-to-read-microsoft-outlook-calendars-with-python-bdf257132318?p=e3308ab07392

CLIENT_ID = 'a4bc8ff9-d31a-4e78-ace4-e923be3d67a0'
SECRET_ID = 'EZV7Q~CbRaetfOXe.ld_x67b-5nZQ58Yydtil'

credentials = (CLIENT_ID, SECRET_ID)
protocol = MSGraphProtocol(default_resource='lvad.mirror@outlook.com')

token_backend = FileSystemTokenBackend(token_path='auth_token', token_filename='auth_token.txt')


scopes = ['Calendars.Read', 'Tasks.Read', 'offline_access']
account = Account(credentials, protocol=protocol, token_backend=token_backend)

if account.authenticate(scopes=scopes):
    print('Authenticated!')

schedule = account.schedule()
calendar = schedule.get_default_calendar()
# events = calendar.get_events(include_recurring=False)
# events = calendar.get_events(query=q, include_recurring=True)
# Time at which the program was started
start_time = float(time.time())
# Counter set to 1 second to execute the following lines immediately
start_counter_sec = 1
# Counter to count how often query was executed
counter = 0

while True:
    # Current time
    current_time = float(time.time())
    # Comparison between time difference (start time and current time and start counter
    # When the difference between current time and start time is bigger than the counter time
    # the auth token and event_list is refreshed.
    if (current_time - start_time) > start_counter_sec:
        counter += 1
        start_counter_sec = 300
        # Resetting the start time
        start_time = float(time.time())
        print(f"Refreshing the auth token ({counter}), here are the events:")

        today = datetime.today()
        yesterday = today - timedelta(days=1)
        thirty_days = today + timedelta(days=30)

        q = calendar.new_query('start').greater_equal(yesterday)
        q.chain('and').on_attribute('end').less_equal(thirty_days)

        schedule = account.schedule()
        calendar = schedule.get_default_calendar()

        cal_query = calendar.get_events(query=q, include_recurring=True)
        event_list = []
        for event in cal_query:
            event_list.append(event)
        print(event_list)

# ********************** Sources **************************** #
# O365 Tutorial:
# https://pietrowicz-eric.medium.com/how-to-read-microsoft-outlook-calendars-with-python-bdf257132318?p=e3308ab07392