set1 = set([int(i) for i in input().split()])
set2 = set([int(i) for i in input().split()])

print(*sorted(set1 & set2), sep=" ")
