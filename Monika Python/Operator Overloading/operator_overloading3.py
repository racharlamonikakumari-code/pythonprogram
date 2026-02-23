class Mycomplex:
  def __init__(self,r,i):
    self.r=r
    self.i=i
  def show(self):
    print (self.r,"+",self.i,"i")
    
c1= Mycomplex(2,3)
c2= Mycomplex(3,4)
c3= Mycomplex(0,0)

c3.r=c1.r+c2.r
c3.i=c1.i+c2.i

c1.show()
c2.show()
c3.show()