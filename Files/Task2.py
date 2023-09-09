"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""


text = "но у меня не получается"

with open("task_2.txt", 'w', encoding="UTF-8") as file:
    file.write(text)

with open("task_1_2.txt", 'w', encoding="UTF-8") as file:
    with open("task_1.txt", 'r', encoding="UTF-8") as file_1:
        text_1 = file_1.read()
    with open("task_2.txt", 'r', encoding="UTF-8") as file_2:
        text_2 = file_2.read()
    file.write(text_1 + ', ' + text_2)