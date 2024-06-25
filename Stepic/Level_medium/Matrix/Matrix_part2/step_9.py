n = int(input())
list_number = [int(i) for i in range(1, n * n + 1)]
matrix = [[int(i) for i in input().split()] for _ in range(n)]
colum = [[0] * n for _ in range(n)]
string = []
main = []
side = []


def chek(colum, string, main, side):
    for i in range(len(colum) - 1):
        if colum[i] == colum[i + 1] and string[i] == string[i + 1]:
            flag1 = True
        else:
            flag1 = False
    if main == side and side == colum[0]:
        flag2 = True
    else:
        flag2 = False
    return flag1 and flag2


for i in range(n):
    main.append(matrix[i][i])
    side.append(matrix[i][n - i - 1])
    for j in range(n):
        if matrix[i][j] in list_number:
            list_number.remove(matrix[i][j])
        colum[j][i] = matrix[i][j]

new_colum = [sum(i) for i in colum]
string = [sum(i) for i in matrix]
main = sum(main)
side = sum(side)


if list_number == [] and chek(new_colum, string, main, side):
    print("YES")
else:
    print("NO")
