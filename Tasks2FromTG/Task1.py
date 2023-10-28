class Work:
    def __init__(self, place: str):
        self.place = place

    def work_info(self):
        print(self.place)


class WorkingStudent(Work):
    def __init__(self, place: str, name: str, placeOfStudying: str):
        super().__init__(place)
        self.name = name
        self.placeOfStudying = placeOfStudying

    def info(self):
        print(self.place, self.name, self.placeOfStudying)


student = WorkingStudent("ITK", "Daniel", "Sirius")
student.info()
