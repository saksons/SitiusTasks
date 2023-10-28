"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""

class SpaceObject:
    def __init__(self, size: int):
        self.size = size


class Star(SpaceObject):
    def __init__(self, size: int, brightness: int):
        super().__init__(size)
        self.brightness = brightness

    def light(self):
        print(f"Яркость: {self.brightness}")


class Planet(SpaceObject):
    def __init__(self, size: int, population: int, annualGrowth: int):
        super().__init__(size)
        self.population = population
        self.annualGrowth = annualGrowth

    def getPopulation(self, years: int):
        return self.population + (self.annualGrowth * years)