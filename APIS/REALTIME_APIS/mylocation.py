import requests

def get_my_location(text):

    response = requests.get(f"http://ip-api.com/json/")
    data = response.json()
    city = data['city']
    state = data['regionName']

    reply = f"Sir, based on the detected coordinates, your current location appears to be {city}, {state}."

    return reply



