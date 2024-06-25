mass = [i for i in input().split()]
new_mass = []
for i in mass:
    if i not in new_mass:
        new_mass.append(i)
print(len(new_mass))

