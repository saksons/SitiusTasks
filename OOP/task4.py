"""
Класс «Автобус». Класс содержит свойства: – speed (скорость), –capacity (максимальное количество пассажиров),
– maxSpeed (максимальная скорость), – passengers (список имен пассажиров), – hasEmptySeats (наличие свободных мест),
– seats (словарь мест в автобусе); методы: – посадка и высадка одного или нескольких пассажиров,
– увеличение и уменьшение скорости на заданное значение.
"""


class Bus:
    def __init__(self, speed: int, capacity: int, maxSpeed: int):
        self.__speed = speed
        self.__capacity = capacity
        self.maxSpeed = maxSpeed
        self.__passengers = []
        self.__hasEmptySeats = True
        self.__seats = {i: True for i in range(0, self.__capacity)}

    def setSpeed(self, speed):
        self.__speed = speed

    def __getFreeSeats(self):
        count = 0
        for i in self.__seats.values():
            if i:
                count += 1
        return count

    def __setHasEmptySeats(self):
        if self.__getFreeSeats() == 0:
            self.__hasEmptySeats = False
            return

    def landingMany(self, count: int, choice: int):
        if choice == 0:
            if self.__getFreeSeats() < count:
                print("Мест на всех не хватит.")
                return
            for i in range(0, count):
                for key, value in self.__seats.items():
                    if value:
                        print(f"{key}: свободное место")
                    else:
                        print(f"{key}: место занято")

                seat = int(input("Введите номер места: "))
                try:
                    if self.__seats[seat]:
                        name = str(input("Введите имя: "))
                        print(f"Новое занятое место: №{seat}")
                        self.__seats[seat] = False
                        self.__passengers.append(name)
                        self.__setHasEmptySeats()
                    else:
                        print(f"Место №{seat} уже занято выберите другое.")
                except:
                    print("Не правильно выбрано место")
                    count+=1

        elif choice == 1:
            if self.__getFreeSeats() == self.__capacity:
                print("Для высадки нет пассажир")
                self.__setHasEmptySeats()
                return

            if (10-self.__getFreeSeats()) < count:
                print("Нет столько людей на высадку.")
                return

            for i in range(0, count):
                for key, value in self.__seats.items():
                    if value:
                        print(f"{key}: свободное место")
                    else:
                        print(f"{key}: место занято")

                seat = int(input("Введите номер места: "))
                try:
                    if self.__seats[seat]:
                        print(f"На месте №{seat} никого нет. Выберите другое место")
                    else:
                        print(f"Пасажир №{seat} был высажен.")
                        self.__seats[seat] = True
                        self.__setHasEmptySeats()
                except:
                    print("Не правильно выбрано место")
                    count+=1




    def landing(self):
        print("0 - посадка\n"
              "1 - высадка")
        choice = int(input())
        if choice < 0 or choice > 1:
            print("Error")
            return

        peoples = int(input("Сколько пассажиров: "))
        if peoples < 1:
            print("Error")
            return
        elif peoples > 1:
            self.landingMany(peoples, choice)
            return

        if choice == 0:
            if not(self.__hasEmptySeats):
                print("Нет мест")
                self.__setHasEmptySeats()
                return

            for key, value in self.__seats.items():
                if value:
                    print(f"{key}: свободное место")
                else:
                    print(f"{key}: место занято")

            while True:
                seat = int(input("Введите номер места: "))
                try:
                    if seat > self.__capacity or seat < 0:
                        self.__setHasEmptySeats()
                        return

                    if self.__seats[seat]:
                        name = str(input("Введите имя: "))
                        print(f"Новое занятое место: №{seat}")
                        self.__seats[seat] = False
                        self.__passengers.append(name)
                        self.__setHasEmptySeats()
                        return
                    else:
                        print(f"Место №{seat} уже занято выберите другое.")
                except:
                    print("Error")
                    return
        elif choice == 1:
            if self.__getFreeSeats() == self.__capacity:
                print("Для высадки нет пассажир")
                self.__setHasEmptySeats()
                return

            for key, value in self.__seats.items():
                if value:
                    print(f"{key}: свободное место")
                else:
                    print(f"{key}: место занято")

            while True:
                seat = int(input("Введите номер места: "))
                try:
                    if seat > self.__capacity or seat < 0:
                        self.__setHasEmptySeats()
                        return

                    if self.__seats[seat]:
                        print(f"На месте №{seat} никого нет. Выберите другое место")
                    else:
                        print(f"Пасажир №{seat} был высажен.")
                        self.__seats[seat] = True
                        self.__setHasEmptySeats()
                        return
                except:
                    print("Error")
                    return

    def debugPrintInfo(self):
        print(self.__speed,
              self.__capacity,
              self.maxSpeed,
              self.__passengers,
              self.__hasEmptySeats,
              self.__seats,
              self.__getFreeSeats())