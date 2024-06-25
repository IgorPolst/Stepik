n = int(input())
total = int(0)
while n > 0:
    if n >= 25:
        n -= 25
        total += 1
    elif n >= 10:
        n -= 10
        total += 1
    elif n >= 5:
        n -= 5
        total += 1
    else:
        n -= 1
        total += 1
print(total)
