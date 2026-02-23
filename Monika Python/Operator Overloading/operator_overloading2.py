class time:
  def __init__(self,h,m,s):
    self.h=h
    self.m=m
    self.s=s
  def __add__(self,other):
    total_hr=self.h+other.h
    total_min=self.m+other.m
    total_sec=self.s+other.s

    if total_sec>=60:
  	  total_sec-=60
  	  total_min+=1

    if total_min>=60:
      total_min-=60
      total_hr+=1	

    return time(total_hr,total_min,total_sec)

  def display(self):
    print(f"{self.h:02}:{self.m:02}:{self.s:02}")

t1=time(5,40,35)
t2=time(4,30,45)
t3=t1+t2
t3.display()      
