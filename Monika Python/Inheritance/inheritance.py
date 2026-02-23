class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        print("Person constructor called")

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def show_info(self):
        print(f"Name: {self._name}, Age: {self._age}")


class Student(Person):
    def __init__(self, name, age, roll, course):
        super().__init__(name, age)
        self._roll = roll
        self._course = course
        print("Student constructor called")

    def set_roll(self, roll):
        self._roll = roll

    def set_course(self, course):
        self._course = course

    def get_roll(self):
        return self._roll

    def get_course(self):
        return self._course

    def show_student_info(self):
        self.show_info()
        print(f"Roll: {self._roll}, Course: {self._course}")


s1 = Student("Monika", 23, 101, "B.Tech")
s1.show_student_info()
