import os
import re
import screen_brightness_control as sbc
from APIS.SYSTEM_APIS.play_on_yt import play_on_yt
from APIS.SYSTEM_APIS.search_on_google import google_search

def system_instruction(text):
    
    text = text.lower()

    #opening/closing software  (using os module)
    if "open" in text and "chrome" in text:
        os.system("start chrome")
        reply = "Chrome has been opened Sir"
        return reply
    elif "close" in text and "chrome" in text:
        os.system("taskkill /f /im chrome.exe")
        reply = "Chrome has been closed Sir"
        return reply
    elif "open" in text and "spotify" in text:
        os.system("start spotify")
        reply = "Spotify has been opened Sir"
        return reply
    elif "close" in text and "spotify" in text:
        os.system("taskkill /f /im Spotify.exe")
        reply = "Spotify has been closed Sir"
        return reply
    elif "open" in text and "youtube" in text:
        os.system("start chrome youtube.com")
        reply = "Youtube has been opened Sir"
        return reply
    elif "open" in text and "task manager" in text:
        os.system("taskmgr")
        reply = "Task Manager has been opened Sir"
        return reply
    


            

    #volume control  (using nircmd + os module)
    elif "volume" in text:
    
        found = re.findall(r'\d+', text)
        
        if found:
            percent = int(found[0]) 
            value = int((percent * 65535) / 100)  
        else:    
            value = None  

        if "increase" in text and value:
            os.system(f"C:\\Tools\\nircmd.exe changesysvolume {value}")
        elif "decrease" in text and value:
            os.system(f"C:\\Tools\\nircmd.exe changesysvolume -{value}")
        elif "set" in text and value is not None:
            os.system(f"C:\\Tools\\nircmd.exe setsysvolume {value}")
        elif "increase" in text:
            os.system("C:\\Tools\\nircmd.exe changesysvolume 6553")  
        elif "decrease" in text:
            os.system("C:\\Tools\\nircmd.exe changesysvolume -6553") 

        reply = "Volume has been changed Sir"

        return reply






    #brightness control ( using screen_brightness_control module)
    elif "brightness" in text:
    
        found = re.findall(r'\d+', text)
        
        if found:
            value = int(found[0])
        else:    
            value = None  

        if "increase" in text and value is not None:
            sbc.set_brightness(f'+{value}')
        elif "decrease" in text and value is not None:
            sbc.set_brightness(f'-{value}')
        elif "set" in text and value is not None:
            sbc.set_brightness(value)
        elif "increase" in text:
            sbc.set_brightness('+10') 
        elif "decrease" in text:
            sbc.set_brightness('-10') 
        #else:
        #    print("No brightness action recognized.")

        reply = "Brightness has been changed Sir"
        return reply
            



    #shutdown/restart/sleep
    elif "shutdown" in text or "reboot" in text or "restart" in text:

        keywords = ["shutdown", "reboot", "restart"]

        for keyword in keywords:
            if keyword in text:
                command = keyword
                break

        confirmation = input("Sir, are you sure you want to " + command + "? (y/n): ")

        if confirmation.lower() == "y":
            if command == "shutdown":
                os.system("shutdown /s /t 2")
                reply = "System is shutting down, Sir"
                return reply

            elif command == "reboot" or "restart":
                os.system("shutdown /r /t 2")
                reply = "System is restarting, Sir"
                return reply

        else:
            print("Action cancelled.")
            reply = "Action cancelled, Sir"
            return reply


    #playing on youtube
    elif "play" in text:
        response = play_on_yt(text)
        return response    
    
    #searching on google
    elif "search" in text:
        response = google_search(text)
        return response

    



           
    



        