m, p = float(input()), float(input())
n = int(input())

for i in range(n):
    s = m * (1 - (p / 100)) ** (i + 1)
    print(i + 1, s)
