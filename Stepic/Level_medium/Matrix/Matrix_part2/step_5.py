n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

for row in matrix:
    print(*row, sep=" ")
