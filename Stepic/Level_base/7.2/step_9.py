m, n = int(input()), int(input())

start = ((m - 1) // 2) * 2 + 1

for i in range(start, n - 1, -2):
    print(i)
