import requests

BASE = 'http://localhost:5000/'

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
    'user': 1,
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

# ----------- CREATE -----------

response = requests.post(BASE + "tasks", json=task)
if response.status_code == 200:
    print(response.status_code)
    print("Record created successfully!")
    print(response.json()) 
else:
    print(response.status_code)
    print("Failed to create record!")
    print(response.text)

# ------------ READ ------------
response = requests.get(BASE + "memberships")

# ----------- UPDATE -----------

# ----------- DELETE -----------

print(response.json())