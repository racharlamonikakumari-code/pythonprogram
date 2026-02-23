#create time class with hours,minutes,seconds ,add two time objects and handle overflow of seconds and minutes
class time:
  def __init__(self,hours,minutes,seconds):
    self.hours=hours
    self.minutes=minutes
    self.seconds=seconds

  def __add__(self,other):
    total_hours=self.hours+other.hours  
    total_minutes=self.minutes+other.minutes
    total_seconds=self.seconds+other.seconds

    total_minutes +=total_seconds//60
    total_seconds=total_seconds%60

    total_hours+=total_minutes//60
    total_minutes=total_minutes%60

    return time(total_hours,total_minutes,total_seconds)

  def __str__(self):
    return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

time1=time(1,48,20)
time2=time(5,65,34)

result=time1+time2

print("Time1=",time1)
print("Time2=",time2)
print("time1+time2=",result)    