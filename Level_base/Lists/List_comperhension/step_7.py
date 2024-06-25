n = int(input())

square = [i**2 for i in range (1,n+1)]
print(*square, sep="\n")