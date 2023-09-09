"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""

def test(one=None, two=None, three=None):
    if one != None and two != None and three != None:
        print(one, two, three)
    else:
        print("NOOOOOOOOOOOOOOOOOOOOOOOOOOne")

test(1)
