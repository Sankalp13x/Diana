import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

engine.say("hello,  good morning  sir my name Thor. I am your personal AI assistant today, there is no live class "
           "what "
           "else I help you?")
engine.runAndWait()