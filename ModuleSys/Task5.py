"""
Напишите скрипт который в качестве параметра из командной строки принимает имя файла. Читает команды в этом файле и выполняет их
Протестируйте скрипт на файле comands.txt
"""

import sys
import os

args = sys.argv

with open(args[1], encoding="UTF-8") as file:
    commands = file.readlines()

for i in commands:
    os.system(f"{i}")