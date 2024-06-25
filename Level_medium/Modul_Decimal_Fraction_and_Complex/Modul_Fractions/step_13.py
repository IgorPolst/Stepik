from fractions import Fraction as F
from math import gcd

n = int(input())
number_set = set()

for chis in range(1, n + 1):
    for znam in range(1, n + 1):
        if F(chis, znam) < 1:
            number_set.add(F(chis, znam))

print(*sorted([i for i in number_set]), sep="\n")
