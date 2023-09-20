"""
Изучите API сервиса https://rickandmortyapi.com/
Получите имя, родную планету и список эпизодов  всех персонажах начиная с вашего номера в журнале и заканчивая ваш номер*5
Сохраните в .json файл.
"""
# no. 16 in the group
import requests
import json

url = "https://rickandmortyapi.com/api/character/1"

start = 16
end = start * 5

data_test = {
    16: {"name": "name, origin",
         "location": "name",
         "episodes": ["episodes"]}
}

data = dict()

for i in range(start, end + 1):
    req = json.loads(requests.get(url=url).text)
    data[i] = {
        "name": f"{req['name']} {req['origin']['name']}",
        "location": req["location"]["name"],
        "episodes": req["episode"]
    }
    print(i)

with open("task3.json", 'w', encoding="utf-8") as file:
    file.write(json.dumps(data, indent=4))
