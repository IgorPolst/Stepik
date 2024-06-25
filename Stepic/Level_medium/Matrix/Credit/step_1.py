mass = [i for i in input().split()]
n = int(input())
mass_group = []
count = 0
for j in range(n):
    mass_group.append(mass[j::n])

print(mass_group)
