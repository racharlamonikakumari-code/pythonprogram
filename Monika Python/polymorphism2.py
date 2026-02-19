class Teacher:
  def role(self):
    print("teaching")		

class Student:
  def role(self):
    print("learning")

def role(persons):
  persons.role()

t=Teacher()
s=Student()

role(t)
role(s)