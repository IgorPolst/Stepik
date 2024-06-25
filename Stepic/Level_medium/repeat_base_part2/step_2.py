mass = [int(i) for i in input().split()]
count = 0
for i in range(1, len(mass)):
    if mass[i - 1] < mass[i]:
        count += 1
print(count)
