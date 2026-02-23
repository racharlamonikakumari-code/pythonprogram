class complex:
  def __init__(self,real,imag):
    self.real=real
    self.imag=imag

  def __repr__(self):
    return'Rational(%s,%s)'% (self.real,self.imag)

  def __str__(self):
    return 'hi %s + i %s' % (self.real,self.imag)

t=complex(10,20)
print(t)
print(str(t))
print(repr(t))