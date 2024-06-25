n = int(input())
list1 = [[1], [1, 1]]
if n == 0:
    print(list1[0])
elif n == 1:
    print(list1[1])
else:
    for i in range(1, n):
        new_list = [1]
        for j in range(len(list1[i]) - 1):
            new_list.append(list1[i][j] + list1[i][j + 1])
        new_list.append(1)
        list1.append(new_list)
    print(list1[n])
