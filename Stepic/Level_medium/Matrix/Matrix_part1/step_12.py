n = int(input())
matrix = []
max = -1000

for _ in range(n):
    list1 = [int(i) for i in input().split()]
    matrix.append(list1)

for i in range(n):
    for j in range(i + 1):
        if matrix[i][j] > max:
            max = matrix[i][j]
print(max)
