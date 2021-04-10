import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyaudio

# Reconhecimento de voz
listener = sr.Recognizer()
# Síntese de fala
engine = pyttsx3.init()
# Velocidade da fala
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5)
# Linguagem da voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
            print('Escutando...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sona' in command:
                command = command.replace('sona', '')
                print(command)
    

# Funções da Sona
def run_sona():
    command = take_command()
    print(command)

    if 'toca' in command:
        song = command.replace('toca', '')
        speak('tocando' + song)
        pywhatkit.playonyt(song)

while True:
    run_sona()
    if len(data) == 0:
        break
