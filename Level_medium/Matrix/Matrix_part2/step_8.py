xy = input()

y = "87654321".index(xy[1])
x = "abcdefgh".index(xy[0])

matrix = [["." for _ in range(8)] for _ in range(8)]
matrix[y][x] = "N"

for i in range(8):
    for j in range(8):
        inx = (x - j) * (y - i)
        if inx == 2 or inx == -2:
            matrix[i][j] = "*"

for row in matrix:
    print(*row, sep=" ")
