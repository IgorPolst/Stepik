a, b = int(input()), int(input())

for i in range(a, b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += 1
    if total == 2:
        print(i)
