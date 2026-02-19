class Laptop:
  def brand(self):
    print("Lenovo")

class Mobile:
  def brand(self):
    print("RealMe")

def brand(appliances):
  appliances.brand()

l=Laptop()
m=Mobile()

brand(l)
brand(m)  