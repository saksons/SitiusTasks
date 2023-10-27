"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""

import random


class Player:
    def __init__(self, id: int, team: str):
        self.id = id
        self.team = team


class Soldiers(Player):
    def __init__(self, id: int):
        super().__init__(id, "Soldier")

    def followingHero(self, hero: object):
        print(f"Солдат с {self.id}, следую за героем {hero.id}")


class Heroes(Player):
    def __init__(self, id: int, rank: str):
        super().__init__(id, "Hero")
        self.__rank = rank
        self.level = 1

    def levelUp(self):
        self.level += 1

    def getRank(self) -> str:
        return self.__rank

    def setRank(self, rank: str) -> None:
        self.__rank = rank

    def removeRank(self):
        self.__rank = None


team_red = []
team_blue = []
oleg = Heroes(1, "Hero")
dima = Heroes(2, "Hero")
team_red.append(oleg)
team_blue.append(dima)
for i in range(3, 24):
    numer = random.randint(1, 2)
    if numer == 1:
        soldier = Soldiers(i)
        team_red.append(soldier)
    else:
        soldier = Soldiers(i)
        team_blue.append(soldier)
print(len(team_red))
print(len(team_blue))
if len(team_red) > len(team_blue):
    team_red[0].levelUp()
    team_red[0].setRank("Победитель арены")
    team_blue[0].removeRank()
else:
    team_blue[0].levelUp()
    team_blue[0].setRank("Победитель арены")
    team_red[0].removeRank()

print(team_red[0].getRank(), team_blue[0].getRank())
