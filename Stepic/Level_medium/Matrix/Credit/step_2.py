n = int(input())
mass = [[int(i) for i in input().split()] for _ in range(n)]
max = 0
if n == 1:
    max = mass[0][0]
else:
    for i in range(n):
        for j in range(n):
            if i + j + 1 >= n:
                if mass[i][j] > max:
                    max = mass[i][j]
print(max)
