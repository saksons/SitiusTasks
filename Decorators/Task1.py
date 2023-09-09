"""
Напишите декоратор печатающий время выполнения данной функции.
"""



# Декоратор пишем тут

import time
def func_to_decor():
    for i in range(5):
        print(i)
        time.sleep(1)


def get_time(func):
    def wrapper():
        start_time = time.time()
        func()
        print(time.time()- start_time)
    return wrapper

decorator = get_time(func_to_decor)
decorator()