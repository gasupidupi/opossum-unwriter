import argparse
import os
import random
from PySide6 import QtCore, QtWidgets, QtGui
from views.fade_view import FadeView
from controllers.fade_controller import FadeController
import sys

def main():
    app = QtWidgets.QApplication([])
    fade_controller = FadeController()
    widget = FadeView(fade_controller)
    widget.resize(245, 410)
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
