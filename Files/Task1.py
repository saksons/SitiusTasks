"""
Напишите программу создающую .txt файл и записывающую туда строку "Я гений и стараюсь учить питон".
Выведите первые 7 символов файла на экран.
"""

text = "Я гений и стараюсь учить питон"

with open("task_1.txt", "w", encoding="UTF-8") as file:
    file.write(text)
with open("task_1.txt", "r", encoding="UTF-8") as file:
    print(file.read()[0:7])