n = int(input())
list1 = []
for i in range(n):
    string = input().split()
    total = 0
    count = 0
    for j in range(n):
        total += int(string[j])
    for j in range(n):
        if int(string[j]) > total / len(string):
            count += 1
    list1.append(count)
print(*list1, sep="\n")
