import requests

BASE = 'http://localhost:5000/'

user = {
    'first_name': 'Alex',
    'last_name': 'Grau',
    'email': 'alexgrau2@email.com',
    'password': 'UsablePassword'
}
trip = {
    'name': 'Grau stimp',
    'start_date': '2023-07-27',
    'end_date': '2023-08-27'
}
membership = {
    'user': 3,
    'trip': 4,
    'owner': 1
}
# ----------- CREATE -----------

response = requests.post(BASE + "memberships", json=membership)
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