a=10
class demo:
  def __init__(self):
    print ("global variable=",a)
  def show (self,b):
    global a
    print ("global variable=",a)
    a=30
  def disp(self):
    print ("global variable=",a)
ob=demo()
ob.disp()
ob.show(50)
print(a)
a=50
print(a)  