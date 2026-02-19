class student:
  def __init__(self,name="unknown"):
    self.name=name
  def show(self):
    print ("name:",self.name)
s1=student()
s2=student("monika")
s1.show()
s2.show()      