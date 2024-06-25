n = int(input())
max1 = 0
max2 = 0
for i in range(n):
    a = int(input())
    if a > max1:
        max2 = max1
        max1 = a
    elif max2 < a < max1:
        max2 = a

print(max1)
print(max2)
