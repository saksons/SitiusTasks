"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""

import csv

a = dict()

with open("Task1.csv", encoding="UTF-8") as file:
    read = csv.reader(file, delimiter=";")
    for row in read:
        if row[0] == "Имя":
            continue
        a[(row[0], row[1])] = {row[2], row[3]}

print(a)
