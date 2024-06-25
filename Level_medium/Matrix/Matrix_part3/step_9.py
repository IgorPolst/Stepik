n, m = [int(i) for i in input().split()]

lst = [[0] * m for _ in range(n)]
nm = 0

for q in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                nm += 1
                lst[i][j] = nm

for row in lst:
    print(*row, sep=" ")
