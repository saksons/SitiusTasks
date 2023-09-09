"""
Выведите из файла character.json Имя персонажа,родную планету и список эпизодов в которых он появлялся.
"""

import json

with open("character.json") as file:
    js = json.loads(file.read())
print(js["name"], js["location"]["name"], js['episode'])