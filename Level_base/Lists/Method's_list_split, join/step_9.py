n = input().split()
k = 0
for i in range (len(n)-1):
    for j in range (i+1,len(n)):
        if n[i] == n[j]:
            k+=1
print(k)