n = int(input())
t1, t2, t3 = 1, 1, 1
list1 = []
for i in range(n):
    list1.append(t1)
    t1, t2, t3 = t2, t3, t1 + t2 + t3
print(*list1)
