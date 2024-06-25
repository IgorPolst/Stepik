n, m = [int(i) for i in input().split()]

matrix = [[str(i * m + j + 1) for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j].ljust(3)
    if i % 2:
        matrix[i].reverse()


for row in matrix:
    print(*row, sep=" ")
