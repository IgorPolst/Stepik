n = int(input())
mass = [["." for _ in range(n)] for _ in range(n)]
for i in range(n):
    mass[i][i] = "*"
    mass[i][n - 1 - i] = "*"
    mass[i][int(n / 2)] = "*"
    mass[int(n / 2)][i] = "*"
for row in mass:
    print(*row, sep=" ")
