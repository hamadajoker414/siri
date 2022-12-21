# Name: mohamed sayed ibrahim       id : 20190907
import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from time import ctime
from gtts import gTTS
import datetime

r = sr.Recognizer()
print(ctime())

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            siri_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="en-uk")
        except sr.UnknownValueError:
            siri_speak('Sorry, I did not get that')
        except sr.RequestError:
           siri_speak('sorry my speach service is down')
        return voice_data

def siri_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio' +str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def Me():
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12:
        siri_speak("Good Morning Mohamed sayed !")
  
    elif hour>= 12 and hour<18:
        siri_speak("Good Afternoon Mohamed sayed !")  
  
    else:
        siri_speak("Good Evening Mohamed sayed !") 
xxx=Me()
  


def respond(voice_data):
    if 'what is your name' in voice_data:
        siri_speak('My name is siri')
    if 'what time is it' in voice_data:
        siri_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        siri_speak('here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('whast is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        siri_speak('here is the location of ' + location)
    if 'open download' in voice_data:
        os.startfile("C:/Users/LENOVO/Downloads")
    if 'where are you from' in voice_data:
        import ipinfo
        handler = ipinfo.getHandler(access_token='2f0b7d20b933b2')
        details = handler.getDetails()
        siri_speak("I'm from " + details.country_name)
    if 'you can go to sleep now' in voice_data:
        siri_speak('bye bye')
        exit()

time.sleep(1)
siri_speak('How can I help you?')
while 1:  
    voice_data = record_audio()
    respond(voice_data)