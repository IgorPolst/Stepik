n = [int(i) for i in input().split()]

matrix = [["." for _ in range(n[1])] for _ in range(n[0])]

for i in range(n[0]):
    for j in range(n[1]):
        if (i + j) % 2 != 0:
            matrix[i][j] = "*"


for row in matrix:
    print(*row, sep=" ")
