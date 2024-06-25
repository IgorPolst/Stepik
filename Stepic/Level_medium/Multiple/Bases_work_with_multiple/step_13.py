n = input()
base = sorted([i for i in n])
chek = sorted(list(set([i for i in n])))

print(base, chek)

if base == chek:
    print("YES")
else:
    print("NO")
