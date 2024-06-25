n = input().split()
flag = True
for i in n:
    if set(n[1]) != set(i):
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
