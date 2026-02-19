class test:
  def __init__(self,x,y):
    self.x=x
    self.y=y
t=test(10,20)
t1=test(30,40)
t2=test(50,60)
print(t.__dict__)
print(t1.__dict__)

print(t2.__dict__)   