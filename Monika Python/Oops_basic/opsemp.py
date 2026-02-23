class employee:
  def __init__(self,n,id,s):
    self.name=n
    self.idcard=id
    self.salary=s
  def show(self):
    print ("emp name=",self.name)
    print ("emp idcard=",self.idcard)
    print ("emp salary=",self.salary)  
E=employee("Akash",101,5000)    
E.show()