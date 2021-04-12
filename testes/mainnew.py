import pyttsx3
import speech_recognition as sr
import datetime
import os
import pywhatkit



# Síntese de fala
engine = pyttsx3.init()
# Linguagem da voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)
# Fala de Sona
def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    speak("Olá Dio.")
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Bom dia Dio!")

    elif hour>=12 and hour<18:
        speak("Boa tarde!")

    elif hour>=18 and hour<24:
        speak("Boa noite!")

    speak("Eu, Soona, estou aqui para lhe ajudar. O que você quer que eu faça?")
def take_command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escutando...")
        audio = r.listen(source)

    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-BR')

    except Exception as e:
        print(e)
        print("Repita por favor...")
        speak("Repita por favor...")
        return "None"
    return query
            
if __name__ == "__main__":
    wishMe()
    while True:
        query = take_command().lower()


        if 'toca' in query:
            query = query.replace("toca", "")
            speak("Tocando " + query)
            print("Tocando" + query)
            


