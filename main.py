import speech_recognition as sr
import pyaudio
import pyttsx3
import datetime

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
   
    if hour>=6 and hour<12:
        speak("Oi bom dia Dio. Tudo bem com você?")

    elif hour>=12 and hour<18:
        speak("Oi boa tarde Dio. Tudo bem com você?")

    elif hour>=18 and hour<24:
        speak("Oi boa noite Dio. Tudo bem com você?")

    else:
        speak("Oi boa noite Dio. Tudo bem com você?")

def meuHumor():
    if 'sim' in takeAudio():
        speak('Que bom. Em que posso te ajudar?')
    elif 'não' in takeAudio():
        speak('Que pena Dio... Estou aqui se precisar, ok??')

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

if __name__ == '__main__':
    while True:
        audio = takeAudio()
        print(audio)

        if 'oi' in audio:
            speak(welcome())
            meuHumor()

        elif audio == 'que horas são' or audio =='qual é a hora':
            speak(SystemInfo.get_time())
        
        elif 'que dia é hoje' or 'data de hoje' in audio:
            speak(SystemInfo.get_date())

        speak('Quais as suas ordens senhor??')
