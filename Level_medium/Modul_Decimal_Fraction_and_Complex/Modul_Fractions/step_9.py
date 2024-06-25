from fractions import Fraction as F

num1, num2 = input(), input()
Fnum1, Fnum2 = F(num1), F(num2)
print(f"{num1} + {num2} = {Fnum2+Fnum1}")
print(f"{num1} - {num2} = {Fnum1-Fnum2}")
print(f"{num1} * {num2} = {Fnum2*Fnum1}")
print(f"{num1} / {num2} = {Fnum1/Fnum2}")
