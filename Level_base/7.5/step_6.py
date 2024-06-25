n = int(input())
max1 = 0
min1 = 10
while n > 0:
    if max1 < n % 10:
        max1 = n % 10
    if min1 > n % 10:
        min1 = n % 10
    n //= 10
print(f"Максимальная цифра равна {max1}")
print(f"Минимальная цифра равна {min1}")
