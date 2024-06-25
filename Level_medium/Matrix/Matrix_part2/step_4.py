n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrix2 = [[matrix[j][i] for j in range(n)] for i in range(n)]
print(f"{matrix} \n {matrix2}")

if matrix == matrix2:
    print("YES")
else:
    print("NO")
