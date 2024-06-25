n = int(input())
mass = []

for  _ in range(n):
    mass.append(int(input()))

mass.remove(max(mass))
mass.remove(min(mass))
print(*mass, sep="\n")