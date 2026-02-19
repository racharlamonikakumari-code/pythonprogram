class time:
  def __init__(self,hours,minutes):
    self.hours=hours
    self.minutes=minutes

  def __add__(self,other_time):
    total_hours=self.hours+other_time.hours
    total_minutes=self.minutes+other_time.minutes

    if total_minutes >= 60:
      total_hours += 1
      total_minutes -= 60

    return time(total_hours,total_minutes)
  
  def __str__(self):
    return f"{self.hours:02d}:{self.minutes:02d}"

time1=time(2,30)
time2=time(1,45)
result=time1+time2
print("time1:",time1)
print("time2:",time2)
print ("time1+time2:",result)