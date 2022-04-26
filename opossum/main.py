import argparse
import os
import random

def main():
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('words_count', type=int,
                    help='A required integer positional argument')
    args = parser.parse_args()
    print(args.words_count)
    cwd = os.getcwd()
    file_paths = os.listdir(cwd)
    random_file_path = random.choice(file_paths)
    file = open(random_file_path, 'r')
    text = file.read()
    random.randing(0,len(text))
    print('Total text:', len(text))

if __name__ == "__main__":
    main()
