import speech_recognition as sr
import pyaudio
import pyttsx3
import datetime
import sys

def takeAudio():
    t = sr.Recognizer()
    with sr.Microphone() as source:
        print('Escutando...')
        audio = t.listen(source)

    data = ''
    try:
        data = t.recognize_google(audio,language="pt-BR")
        data = data.lower()
    except sr.UnknownValueError:
        print('Não consegui entender. Pode repetir?')
        speak('Não consegui entender. Pode repetir?')

    except sr.RequestError as e:
        print('O resultado da Requesição do Google Speech Recognition falhou ' + e)

    return data

def speak(text):    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[-2].id)
    engine.say(text)
    engine.runAndWait()

def welcome():
    hour = int(datetime.datetime.now().hour)

    ask = speak('Com quem estou falando??')
    try:
        answer = takeAudio()
    except sr.UnknownValueError:
        print('Não consegui entender, pode repetir o seu nome?')
        speak('Não consegui entender, pode repetir o seu nome?')
    return answer
    
    if hour>=6 and hour<12:
        speak('Oi bom dia ' + answer)
    

    elif hour>=12 and hour<18:
        speak('Oi boa tarde ' + answer)
        

    elif hour>=18 and hour<24:
        speak('Oi boa noite ' + answer)
        

    else:
        speak('Oi boa noite ' + answer)
        

def meuHumor():
    speak('Tudo bem com você?')
   
    if 'sim' in takeAudio():
        speak('Que bom. Em que posso te ajudar?')
    elif 'não' in takeAudio():
        speak('Que pena ... Estou aqui se precisar de alguma coisa.')

class SystemInfo:
    def __init__(self):
        pass
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos.'.format(now.hour, now.minute)
        return answer

    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        answer = 'Hoje é dia {} do mês {} do ano de {}.'.format(now.day, now.month, now.year)
        return answer

def run_sona():
    audio = takeAudio()
    print(audio)

    if 'oi' in audio:
        speak(welcome())
        meuHumor()

    elif 'que horas são' in audio or 'qual é a hora' in audio:
        speak(SystemInfo.get_time())
        
    elif 'que dia é hoje' in audio or 'data de hoje' in audio:
        speak(SystemInfo.get_date())

while True:
    run_sona()

