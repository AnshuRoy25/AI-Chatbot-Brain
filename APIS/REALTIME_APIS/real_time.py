from APIS.REALTIME_APIS.weather import get_weather_data
from APIS.REALTIME_APIS.mylocation import get_my_location
from APIS.REALTIME_APIS.current_time_date import get_current_time_and_date
from APIS.REALTIME_APIS.googlesearch import google_search

def real_time(user_text):
    
    #weather/temperature/humidity/windspeed
    if "weather" in user_text or "temperature" in user_text or "humidity" in user_text or "windspeed" in user_text:
        response = get_weather_data(user_text)
        return response
    
    #user's location
    elif ("location" in user_text and "my" in user_text) or ("location" in user_text and "current" in user_text): 
        response = get_my_location(user_text)
        return response
    
    #current date and time
    elif ("date" in user_text or "time" in user_text):
        response = get_current_time_and_date(user_text)
        return response
    
    #google search
    else:
        response = google_search(user_text)
        



