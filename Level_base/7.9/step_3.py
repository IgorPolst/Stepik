a, b = int(input()), int(input())
max1 = 0
max2 = 0
sum1 = 0


for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            sum1 += j
    if sum1 >= max1:
        max1 = sum1
        max2 = i
    sum1 = 0
print(max2, max1)
