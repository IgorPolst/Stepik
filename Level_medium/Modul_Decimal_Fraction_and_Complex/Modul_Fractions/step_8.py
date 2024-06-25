from fractions import Fraction as F

num, denum = int(input()), int(input())
print(F(num, denum))


# a,b = num, denum
# while a!=0 and b!=0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a

# print(F(num/(a+b),denum/(a+b)))
