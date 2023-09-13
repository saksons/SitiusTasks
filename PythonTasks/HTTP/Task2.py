"""
Изучите API сервиса https://randomuser.me/
Выведите цитату "Hi, im #NAME, im from #COUNTRY, my phone number is #PHONE"
"""

import requests
import json

url = "https://randomuser.me/api/?format=json"

payload = {

}

req = requests.get(url=url).text
req = json.loads(req)

title = req['results'][0]['name']['title']
first = req['results'][0]['name']['title']
last = req['results'][0]['name']['last']
name = f"{title} {first} {last}"

country = req['results'][0]['location']['country']

phone = req['results'][0]['phone']

print(f"Hi, im {name}, im from {country}, my phone number is {phone}")
