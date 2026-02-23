a=10
class demo:
  def __init__(self):
    self.b=20
  def show(self):
    c=50
    self.c=30
ob=demo()
print(ob.__dict__)
ob.show()
print(ob.__dict__)
ob.d=40 
print (ob.__dict__)     