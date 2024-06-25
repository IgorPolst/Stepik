n, m = [int(i) for i in input().split()]

matrix = [[str(j * n + i + 1) for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j].ljust(3)


for row in matrix:
    print(*row, sep=" ")
