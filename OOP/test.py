import random


class Hero:
    def __init__(self, name: str, power: int, weapon: str):
        self.name = name
        self.health = 100
        self.armor = 100
        self.power = power
        self.weapon = weapon
        print("Inilization class")
        self.printInfo()

    def printInfo(self):
        print(f"name: {self.name}\n"
              f"health: {self.health}\n"
              f"armor: {self.armor}\n"
              f"power: {self.power}\n"
              f"weapon: {self.weapon}\n")

    def fight(self, enemy: object):
        x = random.randint(self.power, self.power * 3)
        if enemy.health < 0 or enemy.health < x:
            print(f"{enemy.name} die")
            return True
        if enemy.armor <= x:
            enemy.health -= x - enemy.armor
            enemy.armor = 0
        elif enemy.armor == 0:
            enemy.health -= x
        else:
            enemy.armor -= x
        self.printInfo()


Knight = Hero("Oleg", 5, "Валына")
Archer = Hero("Ivan", 3, "Лук")

if __name__ == "__main__":
    for i in range(0, 25):
        if Knight.fight(Archer):
            break
        if Archer.fight(Knight):
            break
