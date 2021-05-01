import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from botao1 import *


class Sinais(QtCore.QObject):
    sinal1 = QtCore.pyqtSignal()

class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.sinais = Sinais()
        #self.objeto.signal.connect(self.slot)

        self.ui.pushButton1.clicked.connect(self.funcao1)

    @QtCore.pyqtSlot()
    def funcao1 (self):
        print('Botão 1')
        self.sinais.sinal1.connect(self.recebeSinal)
        self.sinais.sinal1.emit()
        self.sinais.sinal1.disconnect()
    
    def recebeSinal(self):
        ffff

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Tela()
    w.show()
    sys.exit(app.exec_())
