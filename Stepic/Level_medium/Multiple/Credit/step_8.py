m,n = [int(input()) for _ in range (2)]
mathimatic = {input() for _ in range (m)}
phisic = {input() for _ in range (n) }

print(len(mathimatic-phisic))