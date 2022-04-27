from PySide6 import QtCore, QtWidgets, QtGui
import random

class FadeView(QtWidgets.QWidget):

    def __init__(self, fade_controller):
        super().__init__()
        self.fade_controller = fade_controller

        self.name_label = QtWidgets.QLabel(self)
        self.name_label.setText('Words:')
        self.words_line = QtWidgets.QLineEdit(self)

        self.words_line.move(80, 20)
        self.words_line.resize(200, 32)
        self.name_label.move(20, 20)

        pybutton = QtWidgets.QPushButton('OK', self)
        pybutton.clicked.connect(self.fade)
        pybutton.resize(200,32)
        pybutton.move(80, 60)

    @QtCore.Slot()
    def fade(self):
        self.fade_controller.fade(self.words_line.text())
