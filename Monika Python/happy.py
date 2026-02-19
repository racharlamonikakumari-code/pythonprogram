#wap to make range of happy number.    
no=7
T=no
while T!=1 and T!=4:
  print(T)
  s=0
  while T>0:
    digit=T%10
    s=s+digit**2
    T=T//10
  T=s
if T==1:
  print(no,"is a happy number")    