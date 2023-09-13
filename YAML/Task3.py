"""
Сохраните информацию из character.json в yaml файл(Имя файла - ваша фамилия)
"""

import json
import yaml

with open("character.json") as file:
    character = json.loads(file.read())
    print(character)

with open("Safin.yaml", 'w') as file:
    yaml.dump(character, file)