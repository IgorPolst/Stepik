n = input()
x = "abcdefgh".index(n[0])
y = "87654321".index(n[1])
mass = [["." for _ in range(8)] for _ in range(8)]
for i in range(8):
    for j in range(8):
        if ((x + y) == (i + j) or (x - y) == (j - i)) or x == j or y == i:
            mass[i][j] = "*"
mass[y][x] = "Q"
for row in mass:
    print(*row, sep=" ")
