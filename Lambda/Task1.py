"""
Напишите программу которая будет спрашивать пользователя ввод имени пока пользователь не введет off.
Программа должна используя lambda-функцию добавлять к каждому имени надпись "гений".
"""


a = lambda name: name + " гений"
while True:
    name = str(input())
    if name == "off":
        break
    else:
        print(a(name))