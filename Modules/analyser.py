import os, random, requests, shutil
import time

sp_of_days = {
    "понед": "16:00 - тренировка на суше\n"
             "17:00 - тренировка на воде\n",
    "вторн": "7:00 - утреняя тренировка\n"
             "16:00 - тренировка на воде\n",
    "сред":  "7:00 - утреняя тренировка\n"
             "16:00 - тренировка на суше\n",
    "четвер": "Выходной\n",
    "пятн": "Выходной\n",
    "субб": "7:00 - тренировка на суше\n"
            "8:00 - тренировка на воде\n",
    "воскр": "Выходной\n"
}


def main():
    while True:
        req = str(input("--Расписание\n--Данные тренера\n--сумм\n--котик\n--захватить мир\nВведите запрос: ")).lower()
        if req == "off":
            break
        elif "расписание" in req:
            sched(day=req)
        elif ("данн" in req) or ("конт" in req) or ("как узнать" in req) or ("номер" in req):
            contacts(name=req)
        elif ("подсч" in req) or ("сум" in req):
            summ()
        elif ("кот" in req):
            a_vot_i_vse()
        elif ("захват" in req):
            random_function()
        else:
            print("Ошибка, повторите запрос")


def sched(day: str = None):
    finded = False

    for key, value in sp_of_days.items():
        if key in day:
            day = value
            finded = True
            break
        else:
            finded = False

    if finded:
        print(day)
    else:
        print('Не найдено')



def contacts(name: str = None):
    if "ивано" in name:
        print("А вот сам узнай")
    elif "александ" in name:
        print("Номер Александрова: +7 123 456 7890")
    else:
        print("Такого человека нет")


def summ():
    print("Поздравляю ты попал в мою игру. \nЕсли ты не сможешь её пройти твоему компудактеру хана", '\n'*10, "2+2*2")
    num = int(input())
    if num == 6:
        print("Обманул :D \nКомпудактер выключиться через минуту и это не избежать. \nХотяяяяя... \nЕсли ты умный и знаешь некоторые команды, то ты легко сможешь избежать выключение компьютера")
        os.system("shutdown -s -t 60")
    else:
        print("Да ты удачиливый")
    time.sleep(61)
    print("Да ты умный у нас :D")


def random_function():
        print(f"это рандомная функция по запросу \"Как захватить 'что-то'?\". Увы миры захватывать я не умею,\nзато умею выводить рандомные числа 0 или 1 :D \n{random.randint(0,1)}")


def a_vot_i_vse():
    print("Это всё что я умею :(\nНо я умею открывать фотки разных красивых котиков :)")

    r = requests.get("https://cataas.com/cat", stream=True)

    r.raise_for_status()
    r.raw.decode_content = True

    with open('picture.jpg', 'wb') as file:
        shutil.copyfileobj(r.raw, file)

    os.startfile('picture.jpg')




