n = int(input())
total = 0

for i in range(n):
    s = str(input())
    if s.count("11") >= 3:
        total += 1
print(total)
