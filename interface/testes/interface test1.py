from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
import sys


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