n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

matrix.reverse()


def print_matrix(matrix, n, m):
    for c in range(m):
        for r in range(n):
            print(str(matrix[r][c]), end=" ")
        print()
print(matrix)

print_matrix(matrix, n, n)
