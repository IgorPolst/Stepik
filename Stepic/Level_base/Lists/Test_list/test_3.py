mass = [int(i) for i in input().split()]
sum(mass)
print(*mass, sep="+", end=f"={sum(mass)}")
