"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""

import os

os.mkdir("target")

for i in range(10):
    os.mkdir(f"target/{i+1}")