import speech_recognition as sr
import pyaudio
import pyttsx3
import datetime
import pywhatkit
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
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
    except:
        pass


    return data

def speak(text):    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[-2].id)
    engine.say(text)
    engine.runAndWait()

def welcome():
    hour = int(datetime.datetime.now().hour)

    ask = speak('Diga-me seu nome')
    try:
        answer = takeAudio()
    except sr.UnknownValueError:
        print('Não consegui entender, pode repetir o seu nome?')
        speak('Não consegui entender, pode repetir o seu nome?')
    return answer
    
    if hour>=6 and hour<12:
        speak('Oi bom dia ')
    

    elif hour>=12 and hour<18:
        speak('Oi boa tarde ')
        

    elif hour>=18 and hour<24:
        speak('Oi boa noite ')
        

    else:
        speak('Oi boa noite ')
        

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
            
    elif 'toca' in audio:
        musica = audio.replace('toca', '')
        speak('Tocando ' + musica)
        pywhatkit.playonyt(musica)






class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.label_gif = QLabel(self)
        self.label_gif.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gif.move(0,0)
        self.label_gif.resize(720,405)
        self.movie = QMovie("SONACIRCULE.gif")
        self.label_gif.setMovie(self.movie)
        self.movie.start()     

        # Texto "Assistente Virtual"
        self.label_assv = QLabel(self)
        self.label_assv.setText("Assistente Virtual")
        self.label_assv.move(5,5)
        self.label_assv.setStyleSheet('QLabel {font:bold;font-size:14px;color:#FFFFFF}')
        self.label_assv.resize(200,20)

        # Texto "Versão"
        self.label_version = QLabel(self)
        self.label_version.setText("Versão 0.1.3")
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.move(600,380)
        self.label_version.setStyleSheet('QLabel {font-size:14px;color:#FFFFFF}')
        self.label_version.resize(131,20)
        
        # Botão para iniciar a Sona
        iniciar_sona = QPushButton("",self)
        iniciar_sona.move(686,100)
        iniciar_sona.resize(40,40)
        iniciar_sona.setStyleSheet("background-image : url(fecharsona 18x20.png);border-radius: 15px") 
        iniciar_sona.clicked.connect(self.inicarSona)

        # Adiciona a Logo da Sona como um botão sem função
        logo_sona = QPushButton("",self)
        logo_sona.move(225,125)
        logo_sona.resize(259,126)
        logo_sona.setStyleSheet("background-image : url(SonaLogoicone.png);border-radius: 15px") 
         
        # Adiciona uma imagem com função de fechar a aplicação
        botao_fechar = QPushButton("",self)
        botao_fechar.move(686,0)
        botao_fechar.resize(40,40)
        botao_fechar.setStyleSheet("background-image : url(fecharsona 18x20.png);border-radius: 15px") 
        botao_fechar.clicked.connect(self.fechartudo)
        
        self.CarregarJanela()
        
		
    def CarregarJanela(self):
        self.setWindowFlag(Qt.FramelessWindowHint) #sem botoes e titulo
        self.setGeometry(50,50,720,405)
        self.setWindowOpacity(0.90) 
        self.setWindowIcon(QtGui.QIcon('icone.png'))
        self.setWindowTitle("Assistente Virtual")
        self.show()

    def inicarSona(self):
        run_sona()

    def fechartudo(self):
        print('botao fechar presionado')
        sys.exit()

    def mousePressEvent(self, event):
    
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()
    
    def mouseMoveEvent(self, event):
    
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()



aplicacao = QApplication(sys.argv)
j = Janela()
j.show()
sys.exit(aplicacao.exec_())


