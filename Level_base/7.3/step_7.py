from math import *

n = int(input())
count = 0
for i in range(n + 1):
    count += 1 / (i + 1)
count -= log1p(n)
print(count)
