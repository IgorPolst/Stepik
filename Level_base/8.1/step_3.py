n = int(input())
sum_last = 0
sum_3 = 0
sum_1 = 0
sum_5 = 0
sum_5_0 = 0
time = 1
last = n % 10
while n > 0:
    if n % 10 == 3:
        sum_3 += 1
    if last == n % 10:
        sum_last += 1
    if n % 10 % 2 == 0:
        sum_1 += 1
    if n % 10 > 5:
        sum_5 += n % 10
    if n % 10 > 7:
        time *= n % 10
    if n % 10 == 5 or n % 10 == 0:
        sum_5_0 += 1
    n //= 10

print(sum_3)
print(sum_last)
print(sum_1)
print(sum_5)
print(time)
print(sum_5_0)
