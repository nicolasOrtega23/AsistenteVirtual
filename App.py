import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()


nameBot = 'geras'
control = 1

"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
"""
def speak(text):

    engine.say(text)
    engine.runAndWait()

def listener():
    control = 1
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            audio = listener.recognize_google(voice, language='es-ES')
            audio = audio.lower()
            print(audio)

        if nameBot in audio:
            audio = audio.replace(nameBot, '')
            control = run(audio)


        else:
            speak("Intetalo otra vez, no puedo reconocer:  "  + audio)
        
    except sr.UnknownValueError:
        pass
    return control

def run(audio):
    if 'reproduce' in audio:
        music = audio.replace('reproduce', '')
        speak('reproduciedo'  + music)
        pywhatkit.playonyt(music)