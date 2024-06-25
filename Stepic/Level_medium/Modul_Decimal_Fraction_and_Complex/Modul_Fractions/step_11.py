from fractions import Fraction as F
from math import factorial as fac

num = int(input())
summer = 0
for i in range(1, num + 1):
    summer += F(1, fac(i))
print(summer)
