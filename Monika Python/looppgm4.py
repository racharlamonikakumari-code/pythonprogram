#wap find GCD of two numbers. 
no1=12
no2=18
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