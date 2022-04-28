from PySide6 import QtCore, QtWidgets, QtGui
import random
from os.path import expanduser

class FadeView(QtWidgets.QWidget):

    def __init__(self, fade_controller):
        super().__init__()

        self.fade_controller = fade_controller

        self.words_label = QtWidgets.QLabel(self)
        self.words_label.setText('Words:')
        self.words_label.move(20, 70)

        self.words_line = QtWidgets.QLineEdit(self)
        self.words_line.setValidator(QtGui.QIntValidator())
        self.words_line.move(80, 65)
        self.words_line.resize(140, 30)

        self.file_dialog_label = QtWidgets.QLabel(self)
        self.file_dialog_label.resize(500, 30)
        self.file_dialog_label.move(20, 0)

        self.folder_selector = None
        self.file_dialog_button = QtWidgets.QPushButton('project folder', self)
        self.file_dialog_button.clicked.connect(self.open_folder_selector)
        self.file_dialog_button.resize(200,30)
        self.file_dialog_button.move(20, 25)

        self.ok_button = QtWidgets.QPushButton('OK', self)
        self.ok_button.clicked.connect(self.fade)
        self.ok_button.resize(200,30)
        self.ok_button.move(20, 105)

        self.opossum_label = QtWidgets.QLabel(self)
        self.opossum_pixmap = QtGui.QPixmap('./views/pictures/possum.png')
        self.opossum_label.setPixmap(self.opossum_pixmap)
        self.opossum_label.resize(self.opossum_pixmap.width(), self.opossum_pixmap.height())
        self.opossum_label.move(20, 140)



    @QtCore.Slot()
    def open_folder_selector(self):
        self.folder_selector = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Open a folder",
            expanduser("~"),
            QtWidgets.QFileDialog.ShowDirsOnly
        )
        self.file_dialog_label.setText(self.folder_selector)

    @QtCore.Slot()
    def fade(self):
        directory = self.folder_selector
        words_count = self.words_line.text()
        self.fade_controller.fade(directory, words_count)
