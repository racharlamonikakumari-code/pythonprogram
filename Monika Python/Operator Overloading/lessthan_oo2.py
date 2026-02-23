class test:
  def __init__(self):
    self.x=10
    self.y=12.34
  def __str__(self):
    return'{self.x}{self.y}'.format(self=self)
t=test()
print(t)