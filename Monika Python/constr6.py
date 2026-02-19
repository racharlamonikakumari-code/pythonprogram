class test:
  def __init__(self):
     self.x=0
     self.y=0

t=test()
t1=test() 
t2=test()

t.x=10
t.y=20
print(t.x)
print(t.y)

t1.x=30 
t1.y=40
print (t1.x)
print (t1.y)

print (t2.x)
print (t2.y) 

print (t.__dict__)
print (t1.__dict__)
print (t2.__dict__)