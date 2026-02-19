class Dog:
  def sound(self):
    print("bark")

class Cat:
  def sound(self):
    print("meow")

def make_sound(animal):
  animal.sound()

d=Dog()
c=Cat()

make_sound(d)
make_sound(c)          