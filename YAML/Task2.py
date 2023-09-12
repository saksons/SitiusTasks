"""
Из файла info.yaml выведите имя и id Ливерпуля
"""

import yaml

with open("info.yaml") as file:
    liverpul = yaml.safe_load(file)[0]
    print(liverpul["to_name"], liverpul["to_id"])