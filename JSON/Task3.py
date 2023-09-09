"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: [
{
name:***
time:***
cities:***
}
]
"""
task = ["oleg",24,["Belarus","Russia"],(24,1),["Moscow","Vladikavkaz",'Krasnodar',"Rostov","Nalchik"]]

import json

a = {
    "name": task[0],
    "age": task[1],
    "countries": {
        "name": task[2],
        "time": task[3],
        "cities": task[4]
    },
}

with open("Safin_3.json", 'w') as file:
    file.write(json.dumps(a, indent=4))