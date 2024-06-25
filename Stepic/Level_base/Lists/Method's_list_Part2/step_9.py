n = input().split()
seq = []

for el in n:
    seq.append(int(el))

seq.sort()
print(*seq)
seq.sort(reverse=True)
print(*seq)
