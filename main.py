from Prediction_1.ml_classifier import MLClassifier1
from Prediction_2.ml_classifier import MLClassifier2
from Prediction_3.ml_classifier import MLClassifier3
from Query_LLM.query_LLM_Model import QueryLLM
from APIS.SYSTEM_APIS.system import system_instruction
from APIS.REALTIME_APIS.real_time import real_time
from APIS.HARDWARE_APIS.hardware import hardware_instruction
import os
import pyttsx3
import speech_recognition as sr



r = sr.Recognizer()
r.pause_threshold = 1.5  # Wait 1.5 seconds of silence before stopping (default is 0.8)

while True:

    response = None
    with sr.Microphone(device_index=1) as source:
        print("Listening... (speak and pause briefly)")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        user_input = r.recognize_google(audio)
        print(f"You: {user_input}")

        user_input = user_input.lower()

        if "exit" in user_input:
            break

        if not user_input.strip() or len(user_input.strip()) < 3:
            print("Didn't catch that properly. Please try again.")
            continue

    except sr.UnknownValueError:
        print("Could not understand audio")
        continue
    except sr.RequestError:
        print("Google service is unreachable")
        continue

        




    prediction1 = MLClassifier1(user_input) #query / instruction

    print(prediction1)

    if prediction1 == "query":
        prediction2 = MLClassifier2(user_input) # real / normal
        print(prediction2)
        if prediction2 == "normal":
            QueryLLM(user_input)
            
        if prediction2 == "real":
            response = real_time(user_input)
            if response is not None:
               print("Jarvis: ", response)
 

        
    elif prediction1 == "instruction":
        prediction3 = MLClassifier3(user_input)  # system / hardware
        print(prediction3)

        if prediction3 == "system":
            response = system_instruction(user_input)
            print("Jarvis: ", response)
        if prediction3 == "hardware":
            response = hardware_instruction(user_input)   
            print("Jarvis: ", response)
            



    if (prediction1 == "query" and prediction2 == "real" and response is not None) or (prediction1 == "instruction"):
        engine = pyttsx3.init()

        # Optional: set voice, speed, and volume
        engine.setProperty('rate', 170)         # Speed (default is ~200)
        engine.setProperty('volume', 1.0)       # Volume (0.0 to 1.0)

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Try voices[1] for female on Windows

        # Speak the text
        #text = "Sir, i have sucessfully opened chrome!"
        engine.say(response)
        engine.runAndWait()


            





