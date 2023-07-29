import requests

BASE = 'http://localhost:5000/'
EXTENSION = 'users'
ID = '/1'
URL = BASE + EXTENSION

user = {
    'first_name': 'UPDATED',
    'last_name': 'TESTUSER',
    'email': 'updated@email.com',
    'password': 'updated'
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
    'name': 'UPDATED TEST TASK',
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
    'name': 'UPDATE TEST',
    'trip': 1,
    'created_by': 1,
    'from_date': '2023-07-27',
    'from_time': '16:55:34',
    'to_date': '2023-08-01',
    'to_time': '23:59:59'
}

"""

# ----------- CREATE -----------

response = requests.post(URL, json=user)
if response.status_code == 200:
    print(response.json()) 
else:
    print(response.text)

# ----------- UPDATE -----------

response = requests.put(URL + ID, json=event)
print(response.json())
"""
# ----------- DELETE -----------

response = requests.delete(URL + ID, json=user)
print(response.json())

# ------------ READ ------------
response = requests.get(URL)
print(response.json())