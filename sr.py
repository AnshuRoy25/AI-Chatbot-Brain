import speech_recognition as sr

r = sr.Recognizer()
r.pause_threshold = 1.5  # Wait 1.5 seconds of silence before stopping (default is 0.8)

with sr.Microphone(device_index=1) as source:
    print("Listening... (speak and pause briefly)")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError:
    print("Google service is unreachable")