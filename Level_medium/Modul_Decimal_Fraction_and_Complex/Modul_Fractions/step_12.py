from fractions import Fraction as F
from math import gcd

n = int(input())
chis = n // 2
znam = n - chis
while gcd(chis, znam) != 1:
    chis -= 1
    znam += 1
print(F(chis, znam))
