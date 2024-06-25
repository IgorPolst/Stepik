total = 0
for i in range(10):
    n = int(input())
    if n % 2 == 0:
        total += 1
if total == 10:
    print("YES")
else:
    print("NO")
