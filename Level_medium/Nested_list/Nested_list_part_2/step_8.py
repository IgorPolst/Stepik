n = int(input())
print(*[[j + 1 for j in range(n)] for _ in range(n)], sep="\n")