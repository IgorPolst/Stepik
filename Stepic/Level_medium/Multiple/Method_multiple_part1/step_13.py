n = [i.lower().strip(".,;:-?!") for i in input().split()]

print(len(set(n)))
