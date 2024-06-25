n, m = [int(i) for i in input().split()]
matrix = [[int(i) for i in input().split()] for _ in range(n)]

input()

n2, m2 = [int(i) for i in input().split()]
matrix2 = [[int(i) for i in input().split()] for _ in range(n2)]

matrix_result = [[0 for _ in range(m2)] for _ in range(n)]

for i in range(n):
    for j in range(m2):
        for o in range(m):
            matrix_result[i][j] += matrix[i][o] * matrix2[o][j]

for row in matrix_result:
    print(*row, sep=" ")
