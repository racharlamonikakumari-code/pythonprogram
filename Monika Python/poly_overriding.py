class Parent:
  def property(self):
    print("money+car+gold")
  def marry(self):
    print("priyanka")
class Child(Parent):
  def marry(self):
    print("kirti")
c=Child()
c.property()
c.marry()    