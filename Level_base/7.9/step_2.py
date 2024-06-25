n = int(input())
print(1)
for i in range(1, n + 1):
    for j in range(1, i):
        print(j, end="")
    for s in range(i - 1, 0, -1):
        print(s, end="")
    print("")
