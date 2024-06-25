n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
numbers = list(range(1, n + 1))
result = 'YES'

for i in range(n):
    row_nums = sorted(matrix[i])
    col_nums = sorted([matrix[j][i] for j in range(n)])
    if row_nums != numbers or col_nums != numbers:
        result = 'NO'
        break
        
print(result)