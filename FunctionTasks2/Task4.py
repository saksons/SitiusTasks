"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""

def cacluate(*args):
    sr = 0
    for i in args:
        sr += i
    sr_znach = round(sr/len(args))

    vishe_sr = []
    for i in args:
        if i > sr_znach:
            vishe_sr.append(i)
        else:
            continue

    return (sr_znach, vishe_sr)


print(cacluate(100, 1203, 1321, 132))