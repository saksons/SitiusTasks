"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""

import requests

url_cat = "https://cataas.com/cat"
url_cat_original = "https://cataas.com/cat"
url_cat_pixel = "https://cataas.com/cat?width=1&height=1"

a = [url_cat, url_cat, url_cat_original, url_cat_original, url_cat_pixel, url_cat_pixel]
b = 0


def get_pic(url: str, name: str):
    req = requests.get(url=url_cat, stream=True)
    with open(name, 'wb') as file:
        for i in req:
            file.write(i)


for i in a:
    get_pic(i, f"t{b}.jpg")
    b += 1
