n, m = int(input()), int(input())
list1 = []
new_list = []


def print_matrix(matrix, n, m):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]), end=" ")
        print()


for i in range(n):
    new_list = [input() for _ in range(m)]
    list1.append(new_list)


print_matrix(list1, n, m)


# #Короткая генерация матрицы
# n, m = int(input()), int(input())
# matrix = [[input() for _ in range(m)] for _ in range(n)]

# for row in matrix:
#     print(*row)