""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""

import os

os.mkdir("task4")

with open("task4/answer.txt", 'w', encoding="UTF-8") as file:
    file.write("я выполнил задание")