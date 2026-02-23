#Parent class
class Person:
    def _init_(self, name, age):
        self._name = name       # Protected variable (by convention)
        self._age = age
        print("Person constructor called")
    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    # Getter methods
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    # Extra method
    def show_info(self):
        print(f"Name: {self._name}, Age: {self._age}")

# Child class
class Student(Person):
    def _init_(self, name, age, roll, course):
        super()._init_(name, age)  # Call constructor of Person
        self._roll = roll
        self._course = course
        print("Student constructor called")

    # Setter methods
    def set_roll(self, roll):
        self._roll = roll

    def set_course(self, course):
        self._course = course

    # Getter methods
    def get_roll(self):
        return self._roll

    def get_course(self):
        return self._course

    # Extra method
    def show_student_info(self):
        self.show_info()  # Reuse parent method
        print(f"Roll: {self._roll}, Course: {self._course}")

# Create object of Student
s1 = Student("Rahul", 20, 101, "B.Tech")
s1.show_student_info()

# Modify values using setters
s1.set_name("Ravi")
s1.set_age(21)
s1.set_roll(102)
s1.set_course("MCA")

print("\nAfter update:")
s1.show_student_info()