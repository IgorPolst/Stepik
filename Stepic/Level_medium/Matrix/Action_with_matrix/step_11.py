n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
step = int(input())
new_matrix = matrix.copy()

for _ in range(step - 1):
    matrix_result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for o in range(n):
                matrix_result[i][j] += new_matrix[i][o] * matrix[o][j]
    new_matrix = matrix_result

for row in new_matrix:
    print(*row, sep=" ")
