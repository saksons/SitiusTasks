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
    def __init__(self, id: int):
        super().__init__(id, "Hero")
        self.level = 1

    def levelUp(self):
        self.level += 1


team_red = []
team_blue = []
oleg = Heroes(1)
dima = Heroes(2)
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
else:
    team_blue[0].levelUp()
