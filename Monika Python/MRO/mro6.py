class A:
   def __init__(self):
     print("hi")
     self.x=10

class B(A):
  def __init__(self):
    super().__init__()
    print(self.x)
    self.x=20

ob=B()
print(ob.__dict__)       