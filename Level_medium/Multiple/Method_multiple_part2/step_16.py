n = int(input())
set1 = set(input())
for _ in range(n - 1):
    set1.intersection_update(set(input()))

print(*sorted(set1), sep=" ")
