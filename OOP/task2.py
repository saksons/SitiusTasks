class Student():
    def __init__(self, name: str, mark: float, course="-"):
        self.name = name
        self.mark = mark
        self.course = course

    def printInfo(self):
        print(f"Name: {self.name}\n"
              f"Average mark: {self.mark}\n"
              f"course: {self.course}\n")

    def setCourse(self):
        course = str(input())
        self.course = course
        self.printInfo()