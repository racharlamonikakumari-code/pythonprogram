class mycomplex:
  def __init__(self,r,i):
    self._r=r
    self._i=i
  def show(self):
    print(self._r,"+",self._i,"i")
  def __lt__(self,c2):
    if self._r<c2._r and self._i<c2._i:
      return True 
    else:
      return False
c1=mycomplex(2,3)
c2=mycomplex(3,4)
print(c1<c2)