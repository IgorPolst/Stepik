n = int(input())
mass = []

for i in range(n):
    mass.append(int(input()))
del mass[1::2]

print(mass)
