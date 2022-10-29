import speech_recognition as sr
from datetime import datetime
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
activationWord ='hello'

def speak(text, reate=120):
    engine.setProperty('rate', reate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        query = listener.recognize_google(input_speech, language='en_us')
        print(query)
    except Exception as exception:
        #speak("Could u try agin?")
        print("Could u try agin?")
        print(exception)
        return 'None'

    return query

if __name__ == "__main__":
   # speak("Hello All system normal")
    print("Hello All system normal")
    while True:
        query = parseCommand()
        if  activationWord in query:
            query = query.replace(activationWord, "")
            #speak("What should i do?")
            print ("what can i doo")
            if 'stop' in query:
                #speak("The time is")
                print("yhe time is")