import argparse
import os
import random

def main():
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('edit_files_count', type=int,
                    help='A required integer positional argument')
    parser.add_argument('edit_words_count', type=int,
                    help='A required integer positional argument')
    args = parser.parse_args()
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
        index_of_word_to_edit = random.randint(0, len(words)-1)
        print(index_of_word_to_edit)
        words[index_of_word_to_edit] = " "
        new_text = ' '.join(words)
        file.truncate(0)
        file.write(new_text)
        file.close()

        print(new_text)


if __name__ == "__main__":
    main()
