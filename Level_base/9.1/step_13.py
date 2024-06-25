n = str(input())
sum_1 = 0
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        sum_1 += 1
print(sum_1)
