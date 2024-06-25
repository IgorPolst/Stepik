n = int(input())
mass = []

for i in range(1, n + 1):
    if n % i == 0:
        mass.append(i)
print(mass)
