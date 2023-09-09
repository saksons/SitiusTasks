"""
Напишите программу добавляющую в рецепт бутерброда ингридиенты "Салат" и "Ананасы" с помощью декораторов.
"""

def new_ingredients():
    print("Салат")
    print("Ананасы")

def buter(func):
    def wrapper():
        print("Булка")
        print("Мяско")
        print("Сырок")
        func()
        print("Булка")
    return wrapper

dec = buter(new_ingredients)
dec()