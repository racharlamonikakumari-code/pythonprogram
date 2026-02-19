#add time and handle minute overflow 
class time:
  def __init__(self,hours,minutes):
    self.hours=hours
    self.minutes=minutes

  def __add__(self,other):
    total_hours=self.hours+other.hours
    total_minutes=self.minutes+other.minutes

    if total_minutes>=60:
      total_hours += total_minutes // 60
      total_minutes= total_minutes % 60
    
    return time(total_hours,total_minutes)
  
  def __str__(self):
    return f"{self.hours:02d}:{self.minutes:02d}"

time1=time(7,20)
time2=time(5,65)

result=time1+time2

print("Time1=",time1)
print("Time2=",time2)
print("time1+time2=",result)