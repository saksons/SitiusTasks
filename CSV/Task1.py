"""
Из файла Task1.csv выведите данные в формате:
Имя - Звание
"""

import csv


with open("Task1.csv", encoding="UTF-8") as file:
    read = csv.reader(file, delimiter=";")
    for row in read:
        if row[0] == "Имя":
            continue
        print(row[0], row[3])



