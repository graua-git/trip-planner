import json

location = 'API/Endpoints/QueryFunctions/key.json'

def write_key():
    """
    writes new key for API
    """
    key = {
        'key': ''
    }
    with open(location, 'w') as json_file:
        json.dump(key, json_file, indent=4)

def read_key():
    """
    returns key for API
    """
    with open(location, 'r') as json_file:
        data = json.load(json_file)
    return data['key']
