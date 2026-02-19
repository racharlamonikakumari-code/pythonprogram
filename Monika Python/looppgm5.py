#wap Fibbonacci series: 1,3,4,7,11,18....
r=int(input("enter a range:"))
a=1
b=3
print(a,b,end=" ")#end" " as we dont want end\n"
while r>2:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    r=r-1