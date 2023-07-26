import requests

BASE = "http://localhost:5000/"

response = requests.get(BASE + "helloworld/alex/14")
print(response.json())