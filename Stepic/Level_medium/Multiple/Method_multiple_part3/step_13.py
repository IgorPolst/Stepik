student1 = set([int(i) for i in input().split()])
student2 = set([int(i) for i in input().split()])
student3 = set([int(i) for i in input().split()])


print(*sorted(set(int(i) for i in range(11)) - student1 - student2 - student3), sep=" ")
