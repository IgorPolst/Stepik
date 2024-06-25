n = int(input())
sum1 = 0
flag = False
while flag == False:
    while n > 0:
        sum1 += n % 10
        n //= 10
    if sum1 > 9:
        n = sum1
        sum1 = 0
    else:
        flag = True
print(sum1)
