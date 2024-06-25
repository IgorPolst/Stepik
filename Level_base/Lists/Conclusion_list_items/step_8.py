n = int(input())

plus, minus, zero = [],[],[]

for _ in range(n):
    k = int(input())
    if k < 0:
        minus.append(k)
    elif k == 0:
        zero.append(k)
    else:
        plus.append(k)
print (*(minus+zero+plus), sep="\n")