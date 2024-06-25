n = int(input())


def pascal(n):
    list1 = [[1], [1, 1]]
    for i in range(1, n):
        new_list = [1]
        for j in range(len(list1[i]) - 1):
            new_list.append(list1[i][j] + list1[i][j + 1])
        new_list.append(1)
        list1.append(new_list)
    return list1[n]


for i in range(n):
    print(*pascal(i))
