#wap find GCD of two numbers from keyboard.
no1=int(input("enter a numbber1:"))
no2=int(input("enter a numbber2:"))
if no1>=no2:
    N=no1
    D=no2
else:
    N=no2
    D=no1
r=N%D
while r!=0:
    N=D
    D=r
    r=N%D

print ("GCD=",D)
print ("LCM=",no1*no2//D)