class demo:
  def __init__(self):
    self.a=10
    print("local variable=",self.a)
  def show(self,b):
    self.b=40
    print ("local or formal parameter=",self.b)
  def display(self):
    self.c=30
    print ("local variable=",self.c)
ob=demo()
ob.display()
ob.show(50)   
print(ob.a)
print(ob.b)
print(ob.c)     