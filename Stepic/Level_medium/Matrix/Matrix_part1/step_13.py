n = int(input())
matrix = []
max = -1000

for _ in range(n):
    list1 = [int(i) for i in input().split()]
    matrix.append(list1)


def quarters(matrix, number):
    count = 0
    for i in range(n):
        for j in range(n):
            if number == 1 and i < j and i < n - 1 - j:
                count += matrix[i][j]
            elif number == 2 and i < j and i > n - 1 - j:
                count += matrix[i][j]
            elif number == 3 and i > j and i > n - 1 - j:
                count += matrix[i][j]
            elif number == 4 and i > j and i < n - 1 - j:
                count += matrix[i][j]
    return count


for i in range(5):
    if i == 1:
        print(f"Верхняя четверть: {quarters(matrix,i)}")
    elif i == 2:
        print(f"Правая четверть: {quarters(matrix,i)}")
    elif i == 3:
        print(f"Нижняя четверть: {quarters(matrix,i)}")
    elif i == 4:
        print(f"Левая четверть: {quarters(matrix,i)}")
