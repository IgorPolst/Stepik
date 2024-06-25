n = int(input())
mass = []
for _ in range(n):
    mass.append(str(input()))

for  i in range (len(mass)-1):
    k=0
    for j in range(i+1, len(mass)-k):
        print (i,j)
        if mass[i] == mass[j]:
            del mass[j]
            k+=1
print(mass)

