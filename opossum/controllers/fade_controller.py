import argparse
import os
import random
from PySide6 import QtCore, QtWidgets, QtGui
from views.fade_view import FadeView
import sys

class FadeController():

    def __init__(self):
        pass

    def fade(self, words_count):
        cwd = os.getcwd()
        file_paths = os.listdir(cwd)
        filtered_file_paths = []
        for file_path in file_paths:
            if file_path.split('.')[-1] == 'txt':
                filtered_file_paths.append(file_path)
        if len(filtered_file_paths) != 0:
            random_file_path = random.choice(filtered_file_paths)
            file = open(random_file_path, 'r+', encoding='utf-8')

            text = file.read()
            print(text)
            words = text.split()

            for word_count_iterator in range(int(words_count)):
                words.remove(random.choice(words))


            new_text = ' '.join(words)
            file.truncate(0)
            file.write(new_text)
            file.close()

            print(new_text)
