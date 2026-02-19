class test:
  def __init__(self):
    print ("constructor")
  def __del__(self):
    print ("destructor")
t1=test()
t2=test()
t3=test()      