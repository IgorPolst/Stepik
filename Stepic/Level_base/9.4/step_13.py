s = str(input())
max1 = 0
d = 0

for i in s:
    if s.count(i) >= max1:
        max1 = s.count(i)
        d = i
print(d)
