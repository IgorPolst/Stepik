n = int(input())
mass = [[int(i) for i in input().split()] for _ in range(n)]

flag = True
for i in range(n):
    for j in range(n):
        if mass[i][j] != mass[n - j - 1][n - i - 1]:
            flag = False

if flag:
    print("YES")
else:
    print("NO")
