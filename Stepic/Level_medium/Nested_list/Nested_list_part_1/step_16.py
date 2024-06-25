list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
count = 0
for i in list1:
    total += sum(i)
    count += len(i)

print(total / count)
