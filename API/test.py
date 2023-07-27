import requests

BASE = 'http://localhost:5000/'

user = {
    'first_name': 'Alex',
    'last_name': 'Grau',
    'email': 'alexgrau2@email.com',
    'password': 'UsablePassword'
}

# ----------- CREATE -----------

response = requests.post(BASE + "users", json=user)
if response.status_code == 200:
    print(response.status_code)
    print("Record created successfully!")
    print(response.json()) 
else:
    print(response.status_code)
    print("Failed to create record!")
    print(response.text)

# ------------ READ ------------
response = requests.get(BASE + "users")

# ----------- UPDATE -----------

# ----------- DELETE -----------

print(response.json())