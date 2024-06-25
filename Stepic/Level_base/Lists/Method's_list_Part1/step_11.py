n = int(input())
mass = []

for i in range(n):
    number = int(input())
    mass.append(number)
for i in range(n - 1):
    mass[i] += mass[i + 1]
del mass[n - 1]

print(mass)
