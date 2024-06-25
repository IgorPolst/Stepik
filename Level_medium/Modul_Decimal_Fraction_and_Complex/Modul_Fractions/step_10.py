from fractions import Fraction as F

num = int(input())
summer = 0
for i in range(1, num + 1):
    summer += F(1, i**2)
print(summer)
