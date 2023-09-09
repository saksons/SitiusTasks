"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""


import os

def change_name_dir(name):
    for i in os.listdir("target"):
        if int(i)%2 == 0:
            os.rename(f"target/{i}", f"target/{str(name)}_{i}")
            print(f"target/{i}", f"target/{str(name)}")

change_name_dir("soks")

