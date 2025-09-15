from itertools import product

n = int(input())
m = int(input())

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

for comb in product(digits[:n], repeat=m):
    print(''.join(comb), end=' ')
