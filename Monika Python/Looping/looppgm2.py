# wap to make sum of digit to single number.#9+8+7=24=2+4=6
no=987
while no >= 10:
     S = 0
     while no > 0:
	     r = no % 10
	     no = no//10
	     S = S + r
	 no = S
print("sum of digits=",no)