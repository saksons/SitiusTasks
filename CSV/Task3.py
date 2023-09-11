"""
Создайте список предметов формата Название, препод, ваша любовь к предмету(от 0 до 10).
Сохраните в CSV_COMPLETE файл(название файла - ваша фамилия).
P.S не менее 4 столбцов.
"""

import csv

data = [["Название", "препод", "любовь к предмету"],
        ["Matesha", "Boris Igorievich", "100/10"],
        ["Geometry", "Rustem Raymanovich", "-1/10"],
        ["Vvedenie V spec", "Vyachislav Alexandrovich", "10/10"],
        ["Python", "Oleg Babchenok", "1000000000000/10"]]

with open("Safin.csv", 'w', encoding="UTF-8") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)