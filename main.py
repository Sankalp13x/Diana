import speech_recognition as sr
# Speech recognition is an important
# feature used in house automation and
# in artificial intelligence devices.
# The main function of this library is
# it tries to understand whatever the
# humans speak and converts the speech
# to text.
import pyttsx3

# pyttxs3 is a text to speech conversion
# library in python.This package supports
# text to speech engines on Mac os
# x, Windows and on Linux.
import datetime
# This is an inbuilt module in python and
# it works on date and time
import wikipedia
# Wikipedia is a multilingual online
# encyclopedia used by many people from
# academic community ranging from
# freshmen to students to professors who
# wants to gain information over a particular
# topic. This package in python extracts
# data’s required from Wikipedia.
import webbrowser
# This is an in-built package in
# python. It extracts data from the web
import os
# This module is a standard library in
# python and it provides the function
# to interact with operating system
import time
# The time module helps us to display time
import subprocess
# This is a standard library use to
# process various system commands like
# to log off or to restart your PC.

from ecapture import ecapture as ec
# This module is used to capture
# images from your camera
import wolframalpha
# Wolfram Alpha is an API which can compute
# expert-level answers using Wolfram’s algorithms,
# knowledge base and AI technology. It is made
# possible by the Wolfram Language.
import json
# The json module is used for storing
# and exchanging data.
import requests

# The request module is used to send all types
# of HTTP request. Its accepts URL as parameters
# and gives access to the given URL’S.


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')

print('Loading your AI personal assistant - Diana')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

speak("Loading your AI personal assistant Diana")
wishMe()

if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you now  .")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Diana is shutting down,Good bye')
            print('your personal assistant Diana is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Diana version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,'
                  'predict weather '
                  'in different cities , get top headline news from times of india and you can ask me computational '
                  'or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Sankalp")
            print("I was built by Sankalp")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "PW99Q2-L6WY5G88PK"
            client = wolframalpha.Client('PW99Q2-L6WY5G88PK')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
