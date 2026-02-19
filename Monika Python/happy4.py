count = 0
sum_happy = 0
num = 1

while count < 10:
    T = num
    while T != 1 and T != 4:
        temp = 0
        while T > 0:
            digit = T % 10
            temp = temp + digit ** 2
            T = T // 10
        T = temp

    if T == 1:
        sum_happy = sum_happy + num
        count = count + 1

    num = num + 1

print("Sum of first 10 happy numbers =", sum_happy)
