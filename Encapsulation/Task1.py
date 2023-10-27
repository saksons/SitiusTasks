"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""


class BankAccount:
    def __init__(self, name: str, balance: int, pasport: int, password: int):
        self._name = name
        self.__balance = balance
        self.__pasport = pasport
        self.__password = password

    def getPasport(self):
        return self.__pasport

    def getBalance(self):
        return self.__balance
    def setPasport(self, password: int, newPasport: int):
        if self.__password == password:
            self.__pasport = newPasport
            print(f"Номер паспорта изменён на: {newPasport}")
        else:
            print("Пароль не верный")

    def setBalance(self, newBalance):
        if newBalance > 0:
            self.__balance = newBalance
            print(f"Новый баланс: {newBalance}")
        else:
            print("Баланс указан неверно")

    def removePasport(self, password: int):
        if self.__password == password:
            self.__pasport = None
            print(f"Номер паспорта удалён")
        else:
            print("Пароль не верный")



oleg = BankAccount("oleg", 1_000_000, 123456, 123)

print(oleg.getBalance())
print(oleg.getPasport())
print()
oleg.setPasport(654321, 321)
oleg.setPasport(654321, 123)
print()
oleg.setBalance(-12)
oleg.setBalance(5_000_000)
print()
oleg.removePasport(321)
oleg.removePasport(123)
print()
print(oleg.getBalance())
print(oleg.getPasport())




