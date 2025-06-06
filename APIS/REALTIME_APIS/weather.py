import requests
import spacy


def get_weather_data(text):

    #finding cities in user_input
    text = text.title()
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    cities = [ent.text for ent in doc.ents if ent.label_ == "GPE"]

    #finding user's current lat and long
    response = requests.get(f"http://ip-api.com/json/")
    data = response.json()
    lat = data['lat']
    long = data['lon']

    city = cities[0] if cities else None

    if city is not None:
        owm_api = "c91c8df4d9b328b18c9cbd4b0f1c9ebd"
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        parameter = {
            "q": city,
            "appid": owm_api,
            "units": "metric"
        }

        response = requests.get(base_url, params=parameter)
        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
  
        if "weather" in text.lower():
            reply = f"Sir, the current weather in {city} shows a temperature of around {temp}°C, humidity at {humidity}%, and wind speed of approximately {wind_speed} meters per second."
        elif "temperature" in text.lower():
            reply = f"Sir, the current temperature in {city} is around {temp}°"
        elif "humidity" in text.lower():
            reply = f"Sir, the current humidity in {city} is around {humidity}%"
        elif "wind speed" in text.lower():
            reply = f"Sir, the current wind speed in {city} is around {wind_speed}"

    else:
        #reply = "Sorry Sir, I couldn't find the city you're referring to."

        owm_api = "c91c8df4d9b328b18c9cbd4b0f1c9ebd"
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        parameter = {
            "lat": lat,
            "lon": long,
            "appid": owm_api,
            "units": "metric"
        }

        response = requests.get(base_url, params=parameter)
        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
  
        if "weather" in text.lower():
            reply = f"Sir, the current weather in your location shows a temperature of around {temp}°C, humidity at {humidity}%, and wind speed of approximately {wind_speed} meters per second."
        elif "temperature" in text.lower():
            reply = f"Sir, the current temperature in your location is around {temp}°"
        elif "humidity" in text.lower():
            reply = f"Sir, the current humidity in location is around {humidity}%"
        elif "wind speed" in text.lower():
            reply = f"Sir, the current wind speed in your location is around {wind_speed}"
    
                                                                   
    return reply

