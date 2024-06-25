n = int(input())
total = 0

for i in range(n + 1):
    print(i)
    if n % (i + 1) == 0:
        total += i + 1
        print(n, i, total)
print(total)
