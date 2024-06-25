n, m = int(input()), int(input())
matrix = []
list1 = []


def print_matrix(matrix, n, m):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]), end=" ")
        print()


matrix = [[str(i * j).ljust(3) for i in range(m)] for j in range(n)]


print_matrix(matrix, n, m)
