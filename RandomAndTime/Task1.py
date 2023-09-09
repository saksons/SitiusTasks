"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""
import sys
import time
from threading import Thread


start_time = time.time()


def hop():
    while True:
        if input("Введите ход: ") == "off":
            sys.exit()
        else:
            print("у вас осталось: ", 1800 - (time.time() - start_time), "секунд")

def lose_time():
    time.sleep(1800)
    sys.exit()

th1 = Thread(target=lose_time, args=()).start()
th2 = Thread(target=hop, args=()).start()
