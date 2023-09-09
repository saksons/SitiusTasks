"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.
"""

import sys

args = sys.argv

with open(f"{args[2]}.txt",'w') as file:
    file.write(args[1])