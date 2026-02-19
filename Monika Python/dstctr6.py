class test:
  def __init__(self):
    print ("constructor")
  def __del__(self):
    print ("destructor")
  def show(self):
    print ("show funtion start")
    t2=test()
    print ("show function end")
t1=test()
t1.show()
t3=test()        