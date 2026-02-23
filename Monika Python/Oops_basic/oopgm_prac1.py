# create a class Time that stores hours and minutes..overload + operator to add two time objects .
class time:
  def __init__(self,hours,minutes):
    self.hours=hours
    self.minutes=minutes

  def __add__(self,other):
    total_hours=self.hours+other.hours
    total_minutes=self.minutes+other.minutes
    return time (total_hours,total_minutes)

  def __str__(self):
    return f"{self.hours:02d}:{self.minutes:02d}"

time1=time(2,45)
time2=time(4,28)
result=time1+time2

print("time1:",time1)
print("time2:",time2)
print("time1+time2:",result) 

