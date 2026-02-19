class student:
  def __init__(self,n):
    self.n=n
  def show (self):
    print("n=",self.n)
obj=student("akash")
obj.show()
obj1=student("monika")
obj1.show()