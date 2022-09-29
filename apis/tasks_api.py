import requests
import msal
import atexit
import os.path
import time

# from api_output import task_info_extract

# ********************** Sources **************************** #
# MSAL with Python Tutorial:
# https://gist.github.com/darrenjrobinson/553ea10e304246ebfa1eac6dde0cf63b
# https://blog.darrenjrobinson.com/microsoft-graph-using-msal-with-python-and-delegated-permissions/

TENANT_ID = 'd2eb11aa-b2ee-4569-97ee-116212117380'
CLIENT_ID = '9633f396-97a7-4d53-8bad-bae60413b663'

AUTHORITY = 'https://login.microsoftonline.com/common'
# AUTHORITY = 'https://login.microsoftonline.com/' + TENANT_ID
ENDPOINT = 'https://graph.microsoft.com/v1.0'
LIST_ID = 'AQMkADAwATM3ZmYAZS00OGE2LTRhMjYtMDACLTAwCgAuAAAD0tY4K1iZrE2ob7wNmmZZyAEA2rEe84gaAkWI9CWBkgJRogAAAAUreXUAAAA='

SCOPES = ['Tasks.Read']

cache = msal.SerializableTokenCache()

if os.path.exists('token_cache_task.bin'):
    cache.deserialize(open('token_cache_task.bin', 'r').read())

atexit.register(lambda: open('token_cache_task.bin', 'w').write(cache.serialize()) if cache.has_state_changed else None)

app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY, token_cache=cache)

accounts = app.get_accounts()
result = None

# Time at which the program was started
start_time = float(time.time())
# Counter set to 1 second to execute the following lines immediately
start_counter_sec = 1
# Counter to count how often query was executed
counter = 0
task_list = []
test_var = "TEST"


def task_info_extract(input_data, input_num):
    for n in range(0, input_num):
        task_row = input_data['value'][n]
        task_name = task_row['title']
        task_status = task_row['status']
        task_created_date = task_row['createdDateTime'][0:10]
        if 'completedDateTime' in task_row:
            task_completed_date_row = (task_row['completedDateTime'])
            task_completed_date = (task_completed_date_row['dateTime'][0:10])
            task_dict = {'title': task_name, 'status': task_status, 'created_date': task_created_date,
                         'completed_date': task_completed_date}
            task_list.append(task_dict)
        else:
            task_dict = {'title': task_name, 'status': task_status, 'create_date': task_created_date}
            task_list.append(task_dict)

    return task_list


while counter < 10:
    # Current time
    current_time = float(time.time())
    # Comparison between time difference (start time and current time and start counter
    # When the difference between current time and start time is bigger than the counter time
    # the auth token and event_list is refreshed.
    if (current_time - start_time) > start_counter_sec:
        counter += 1
        # Resetting the start time
        start_time = float(time.time())
        start_counter_sec = 1

        if len(accounts) > 0:
            result = app.acquire_token_silent(SCOPES, account=accounts[0])

        if result is None:
            flow = app.initiate_device_flow(scopes=SCOPES)
            if 'user_code' not in flow:
                raise Exception('Failed to create device flow')

            print(flow['message'])

            result = app.acquire_token_by_device_flow(flow)

        if 'access_token' in result:

            result = requests.get(f'{ENDPOINT}/me/todo/lists/{LIST_ID}/tasks',
                                  headers={'Authorization': 'Bearer ' + result['access_token']})
            result.raise_for_status()
            task_data_row = result.json()
            task_data_length = len(task_data_row['value'])
            # Cleaning the task list to refill it afterwards
            task_list = []
            task_info_extract(task_data_row, task_data_length)
            # print("Program started at 18:55")
            print(f"Refreshing the auth token ({counter}), here are the tasks:")
            print("From Task API:", task_list)

        else:
            raise Exception('No access token in result')

# ********************** Sources **************************** #
# MSAL with Python Tutorial:
# https://gist.github.com/darrenjrobinson/553ea10e304246ebfa1eac6dde0cf63b
# https://blog.darrenjrobinson.com/microsoft-graph-using-msal-with-python-and-delegated-permissions/
