mass = input().split()
print(mass)
for n in range(len(mass)):
    mass = [i[1:]+i[0]+"ки" for i in mass[n]]
print(*mass)
