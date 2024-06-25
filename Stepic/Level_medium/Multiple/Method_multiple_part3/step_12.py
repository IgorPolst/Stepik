student1 = set([int(i) for i in input().split()])
student2 = set([int(i) for i in input().split()])
student3 = set([int(i) for i in input().split()])


print(*sorted(student3 - (student2 | student1), reverse=True), sep=" ")
