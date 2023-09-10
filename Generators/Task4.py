"""
Напишите генераторное выражения. Для генерации словаря где ключем выступают числа от 0 до 10. А значения эти же числа в 16чной системе счисления.
Работу с 16чной системой найдите в документации Python
"""

import random

a = dict()

def getDict(test: dict):
    num = random.randint(0,10)
    test[num] = hex(num)
    yield test


for i in range(0,5):
    next(getDict(a))

print(a)