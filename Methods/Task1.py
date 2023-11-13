"""
Создайте класс Person у которого будут свойства name и age.
Добавьте метод экземпляра который выводит информацию о человеке.
Создайте метод класса который генерирует новый объект класса
который ставить возраст человека: сегодняшний год - год который передают в метод.
(подсказка: тут можно использовать метод today().year класса date из модуля datetime)
Создайте статический метод который проверяет является ли совершеннолетним человек возраст которого передается в метод.
"""

import datetime


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def printInfo(self):
        print(self.name, self.age)

    @classmethod
    def personClassmethod(cls) -> None:
        person = cls("Jhon", datetime.date.today().year)

    @staticmethod
    def personStaticmethod(age) -> bool:
        if (datetime.date.today().year - age) >= 18:
            return True
