"""
Напишите список функций по требованию. Пользователь вводит имя.
Если имя заканчивается на А,Я,Г,М, то программа добавляет к имени "Гений".
Если на О,Ь,Л,Н. То добавляется "Сверхразум". Если ни на одну из этих букв то добавляется "Просто" перед именем.
"""


def A(name: str):
    print(f"{name} Гений")


def O(name: str):
    print(f"{name} Сверхгений")


def test(name: str):
    if (name[-1] in ['А', 'Я', 'Г', 'М']):
        A(name=name)
    elif (name[-1] in ['О', 'Ь', 'Л', 'Н']):
        O(name=name)


test(str(input()))