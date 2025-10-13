n = int(input())

field = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        field[i][j] = min(i, j, n - 1 - i, n - 1 - j) + 1

for row in field:
    print(*row)