
import os
import glob

if __name__ == "__main__":
    for filename in glob.iglob('c:\\sandbox\\**\\.picasa.ini', recursive=True):
        with open(filename, 'r') as fin:
            print(fin.read())
