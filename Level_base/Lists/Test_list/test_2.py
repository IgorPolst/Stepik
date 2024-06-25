mass1 = [int(i) for i in input().split()]
mass2 = [int(i) for i in input().split()]
print(*[mass1[i] + mass2[i]for i in range(len(mass1))])