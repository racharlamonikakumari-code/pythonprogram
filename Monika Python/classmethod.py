class demo:
  count=10
  @classmethod
  def update_count(cls):
    cls.count+=1
    print("count=",cls.count)
demo.update_count()    