n = int (input())
mass = []
sqr = []
for _ in range(n):
    x = int(input())
    mass.append(x)
    sqr.append(x**2+2*x+1)
print (*mass, sep = "\n")
print()
print (*sqr, sep = "\n")