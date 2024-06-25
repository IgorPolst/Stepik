n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrix_index = [int(i) for i in input().split()]

for i in range(n):
    matrix[i][matrix_index[0]], matrix[i][matrix_index[1]] = (
        matrix[i][matrix_index[1]],
        matrix[i][matrix_index[0]],
    )


for row in matrix:
    print(*row, sep =" ")
