class mycomplex:
  def __init__(self,r,i):
    self._r=r
    self._i=i
  def show(self):
    print(self._r,"+",self._i,"i")
  def __sub__(self,c2):
    c3=mycomplex(0,0)
    c3._r=self._r-c2._r
    c3._i=self._i-c2._i
    return c3
c1=mycomplex(2,3)
c2=mycomplex(3,4)
c3=c1-c2
c1.show()
c2.show()
c3.show()        