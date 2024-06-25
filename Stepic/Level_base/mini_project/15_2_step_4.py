n = int(input())
total = 0
left = 1
right = n
middle = -1
while right > left:
    middle = (left + right) // 2
    total += 1
    right = middle
print(total)
