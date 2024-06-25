student = [tuple(input().split()) for _ in range(int(input()))]
good_student = []


for i in student:
    print(*i, sep=" ")
print()
for i in student:
    if i[1] > 3:
        print(*i, sep=" ")
