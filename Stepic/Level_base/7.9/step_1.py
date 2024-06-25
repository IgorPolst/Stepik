n = int(input())
total = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(total, end=" ")
        total += 1
    print("")
