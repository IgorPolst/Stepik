n = int(input())
mass = [[int(i) for i in input().split()] for _ in range(n)]
new_mass = mass.copy()
for i in range(n):
    for j in range(n):
        print(mass[j][i], end=" ")
    print()
