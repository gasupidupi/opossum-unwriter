import os
import random


class FadeController():

    def __init__(self):
        pass

    def fade(self, directory, words_count):
        file_names = os.listdir(directory)
        filtered_file_names = []
        for file_name in file_names:
            if file_name.split('.')[-1] == 'txt':
                filtered_file_names.append(file_name)
        if len(filtered_file_names) == 0 or not directory:
            return 0
        random_file_name = random.choice(filtered_file_names)
        file_r = open(
            os.path.join(directory, random_file_name),
            'r',
            encoding='utf-8'
        )
        text = file_r.read()
        file_r.close()
        file_w = open(
            os.path.join(directory, random_file_name),
            'w',
            encoding='utf-8'
        )
        words = text.split()
        for word_count_iterator in range(int(words_count)):
            if len(words) == 0:
                break
            words.remove(random.choice(words))
        new_text = ' '.join(words)
        file_w.truncate(0)
        file_w.write(new_text)
        file_w.close()
