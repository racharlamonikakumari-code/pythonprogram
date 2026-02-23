class test:
  def __init__(self,x):
    self.x=x
    print("constructor")
  def __del__(self):
    print ("destructor",self.x)  
  def show(self):
    print ("show function start")
    t2=test(20)
    print ("show function end")
t1=test(10)
t1.show()
t3=test(30)      