from math import factorial

n = int(input())

sum1 = 0

for i in range(1, n + 1):
    sum1 += factorial(i)
    print(sum1)
print(sum1)
