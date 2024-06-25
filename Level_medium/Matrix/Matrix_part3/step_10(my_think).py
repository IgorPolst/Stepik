n, m = [int(i) for i in input().split()]
list_number = [int(i) for i in range(1, n * m+1)]
matrix = [[0] * m for _ in range(n)]
repeat = 1
i = 0
j = 0
count = 0


def move_right(i, j, matrix, number, list_number):
    matrix[i][j] = number
    j += 1
    list_number.remove(number)
    return j, matrix


def move_left(i, j, matrix, number, list_number):
    matrix[i][j] = number
    j -= 1
    return j, matrix


def move_up(i, j, matrix, number, list_number):
    matrix[i][j] = number
    i -= 1
    return i, matrix


def move_down(i, j, matrix, number, list_number):
    matrix[i][j] = number
    i += 1
    return i, matrix


for number in list_number:
    if j < m - repeat and matrix[i][j + 1] == 0:
        j, matrix = move_right(i, j, matrix, number)

    elif i < n - repeat and matrix[i + 1][j] == 0:
        move_down(i, j, matrix, number)
    elif j > 0 + repeat and matrix[i][j + 1] == 0:
        move_left(i, j, matrix, number)
    elif i > 0 + repeat and matrix[i + 1][j] == 0:
        move_up(i, j, matrix, number)


for row in matrix:
    print(*row, sep=" ")
