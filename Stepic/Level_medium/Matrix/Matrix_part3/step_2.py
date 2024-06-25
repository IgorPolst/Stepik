n = int(input())

matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if n - i - 1 == j:
            matrix[i][j] = 1
        elif n - i - 1 < j:
            matrix[i][j] = 2


for row in matrix:
    print(*row, sep=" ")
