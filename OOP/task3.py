class Rectangle:
    def __init__(self):
        self.width = int(input())
        self.height = int(input())

    def draw(self):
        print('#' * self.width)
        for i in range(0, self.height):
            print(f"#{' ' * (self.width - 2)}#")
        print('#' * self.width)

    def printInfo(self):
        print(f"Дан прямоугольник с длиной {self.width} и шириной {self.height}.")

    def perimeter(self):
        print(2 * (self.width + self.height))

    def square(self):
        print(self.width * self.height)