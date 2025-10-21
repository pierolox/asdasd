import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/calculadora.ui", self)
    
    def botones(self):
        self.btn0 = "0"
        self.btn1 = "1"
        self.btn2 = "2"
        self.btn3 = "3"
        self.btn4 = "4"
        self.btn5 = "5"
        self.btn6 = "6"
        self.btn7 = "7"
        self.btn8 = "8"
        self.btn9 = "9"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Calculadora()
    GUI.show()
    sys.exit(app.exec_())