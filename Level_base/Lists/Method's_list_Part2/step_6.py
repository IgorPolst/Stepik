n = input()
mass = []
mass = n.split()
for i in range(len(mass)):
    mass[i] = int(mass[i])


bufer = max(mass)
bufer_index = mass.index(max(mass))
bufer_index2 = mass.index(min(mass))
print(bufer, bufer_index, bufer_index2)
mass[bufer_index] = min(mass)
mass[bufer_index2] = bufer

for i in range(len(mass)):
    mass[i] = str(mass[i])

print(" ".join(mass))


# seq = []
# for el in input().split():
#     seq.append(int(el))
    
# mx_ind = seq.index(max(seq))
# mn_ind = seq.index(min(seq))
# seq[mx_ind], seq[mn_ind] = seq[mn_ind], seq[mx_ind]

# print(*seq)