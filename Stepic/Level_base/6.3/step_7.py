from math import *

a, b, c = float(input()), float(input()), float(input())
D = b**2 - 4 * a * c

if a != 0 and D >= 0:
    if D == 0:
        print(-b / (2 * a))
    else:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / (2 * a)
        print(min(x1, x2))
        print(max(x1, x2))
else:
    print("Нет корней")
