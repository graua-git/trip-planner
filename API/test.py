import requests

BASE = 'http://localhost:5000/'
EXTENSION = 'memberships'
URL = BASE + EXTENSION

user = {
    'first_name': 'TEST',
    'last_name': 'USER',
    'email': 'testuser@email.com',
    'password': 'TESTPassword'
}
trip = {
    'name': 'TEST TRIP',
    'start_date': '2023-07-27',
    'end_date': '2023-08-27'
}
membership = {
    'user': 5,
    'trip': 1,
    'owner': 0
}
task = {
    'name': 'TEST TASK',
    'trip': 1,
    'assignee': 1,
    'created_by': 1,
    'date_created': '2023-07-27',
    'time_created': '16:55:34',
    'due_date': '2023-08-01',
    'due_time': '23:59:59'
}
expense = {
    'name': 'TEST EXPENSE',
    'trip': 1,
    'owed_to': 1,
    'owed_by': 2,
    'date_created': '2023-07-27',
    'time_created': '16:55:34',
    'amount': 12345.67,
    'settled': 0
}
event = {
    'name': 'TEST EVENT',
    'trip': 1,
    'created_by': 1,
    'from_date': '2023-07-27',
    'from_time': '16:55:34',
    'to_date': '2023-08-01',
    'to_time': '23:59:59'
}

# ----------- CREATE -----------

response = requests.post(URL, json=membership)
if response.status_code == 200:
    print(response.status_code)
    print("Record created successfully!")
    print(response.json()) 
else:
    print(response.status_code)
    print("Failed to create record!")
    print(response.text)

# ------------ READ ------------
response = requests.get(URL)

# ----------- UPDATE -----------

# ----------- DELETE -----------

print(response.json())