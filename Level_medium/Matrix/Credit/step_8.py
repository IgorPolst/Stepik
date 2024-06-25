n = int(input())
mass = [[0] * n for _ in range(n)]
new_mass = mass.copy()
count = 1
for i in range(n):
    for j in range(n):
        if i < j:
            mass[i][j] += count
            count += 1
    count = 1

for j in range(n):
    for i in range(n):
        new_mass[i][j] = mass[j][i]


for row in mass:
    print(*row, sep=" ")
