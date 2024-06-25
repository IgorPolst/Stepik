import random

n = 10**6
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)  # случайное число с плавающей точкой от 0 до 1
    y = random.uniform(-2, 2)  # случайное число с плавающей точкой от 0 до 1

    if x**3 + y**4 + 2 >= 0 and 3 * x + y**2 <= 2:  # если попадает в нужную область
        k += 1

print((k / n) * s0)
