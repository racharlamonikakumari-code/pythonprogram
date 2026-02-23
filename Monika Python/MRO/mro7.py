class A:
  @classmethod
  def show(cls):
    print("show class function")
  @staticmethod
  def disp():
    print("disp static method")
class B(A):
    pass
B.show()
B.disp()        