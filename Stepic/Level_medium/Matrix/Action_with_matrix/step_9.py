n, m = [int(i) for i in input().split()]

matrix = [[int(i) for i in input().split()] for _ in range(n)]
input()
matrix2 = [[int(i) for i in input().split()] for _ in range(n)]
matrix_result = [[0 for _ in range(m)] for _ in range(n)]
print(matrix, matrix_result)
for i in range(n):
    for j in range(m):
        matrix_result[i][j] = matrix[i][j] + matrix2[i][j]

for row in matrix_result:
    print(*row, sep=" ")
