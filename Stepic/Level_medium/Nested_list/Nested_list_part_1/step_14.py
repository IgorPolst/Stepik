list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = 0
for i in list1:
    if maximum < max(i):
        maximum = max(i)


print(maximum)
