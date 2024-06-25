n = int(input())
print(*[[j for j in range(1, i + 2)] for i in range(n)], sep="\n")
