from datetime import datetime

def get_current_time_and_date(text):

    now = datetime.now()

    date_str = now.strftime("%B %d, %Y")       
    time_str = now.strftime("%I:%M %p")  

    if "date" in text and "time" in text:
        reply = f"Sir, the current date is {date_str} and the time is {time_str}."
        return reply
    elif "date" in text: 
        reply = f"Sir, today's date is {date_str}."
        return reply
    elif "time" in text:
        reply = f"Sir, the current time is {time_str}."
        return reply
    

