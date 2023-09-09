"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: ***
"""
task = ["oleg",24,["Belarus","Russia"]]

import json

a = {
    "name" : task[0],
    "age": task[1],
    "countries": task[2]
}

with open("Safin_2.json", 'w') as file:
    file.write(json.dumps(a, indent=4))