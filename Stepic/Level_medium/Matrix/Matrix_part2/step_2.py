n, m = int(input()), int(input())
matrix = []
max = -1000
list_index = [0, 0]
for _ in range(n):
    list1 = [int(i) for i in input().split()]
    matrix.append(list1)

for i in range(n):
    for j in range(m):
        if matrix[i][j] > max:
            max = matrix[i][j]
            list_index[0], list_index[1] = i, j
print(*list_index, sep=" ")
