s = 0
total = 0
for i in range(7):
    n = int(input())
    if n % 2 == 0:
        s += n
        total += 1
if total == 0:
    print(0)
else:
    print(s)
