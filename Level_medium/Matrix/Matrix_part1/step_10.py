n = int(input())
matrix = [input().split() for _ in range(n)]
matrix = [[int(matrix[i][j]) for j in range(n)] for i in range(n)]
total = 0
for i in range(n):
    total += matrix[i][i]

print(total)
