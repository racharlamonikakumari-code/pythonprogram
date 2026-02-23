class student:
  def set (self,n,r,m):
    self.name=n
    self.roll=r
    self.mark=m
  def show(self):
    print ("my name=",self.name)
    print ("my rollno=",self.roll)
    print ("my mark=",self.mark)
s=student()
s.set("monika",1,90.25)
s.show()      