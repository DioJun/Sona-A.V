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

    if audio == 'sona' or 'oi':
        speak('Oi Dio! Tudo bem com você?')
    
    if audio == 'tudo sim':
         speak('Que bom! Em que posso ser útil?')

    if audio == 'que horas são' or 'qual é a hora':
        speak(SystemInfo.get_time())

while True:
    run_sona()
