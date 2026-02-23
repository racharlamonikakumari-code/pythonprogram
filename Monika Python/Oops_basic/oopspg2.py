class student:
  def __init__(self,name,roll,mark):
    self.name= name
    self.roll= roll
    self.mark= mark
    print ("constructor called")
  def display(self):
    print("name:",self.name)
    print("roll:",self.roll)
    print("mark:",self.mark)
s1=student("monika",1,90)
s1.display()    