string = [i for i in input().split()]
print(string[-1], *string[0 : len(string) - 1])
