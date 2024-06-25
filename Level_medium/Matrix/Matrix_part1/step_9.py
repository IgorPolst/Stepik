n, m = int(input()), int(input())

#Печать матрицы по строкам и по колонкам
def print_matrix(matrix, n, m):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]), end=" ")
        print()
    print("\n")
    for c in range(m):
        for r in range(n):
            print(str(matrix[r][c]), end=" ")
        print()

#Создание матрицы
def generat_matrix(n, m):
    list1 = []
    new_list = []
    for _ in range(n):
        new_list = [input() for _ in range(m)]
        list1.append(new_list)
    return list1

work_list = generat_matrix(n,m)
print_matrix(work_list, n, m)
