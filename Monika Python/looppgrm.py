 #wap to find armstrong number :total digit count to be used ad power 
 no=153
 T=no
 p=0
 #count number of digit 
 while T!=0:
       p=p+1
       T=T//10
S=0 
T=no      
while T!=0:
     r=T%10
     S=S+r**p
     T=T//10
if S==no: 
    print (s,"Number is Armstrong")

    