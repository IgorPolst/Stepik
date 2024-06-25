mass = [int(i) for i in input().split()]

for i in range(0, len(mass) - 1, 2):
    mass[i], mass[i + 1] = mass[i + 1], mass[i]

print(*mass, sep = " ")
