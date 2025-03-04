from collections import Counter
from functools import reduce

products = dict(Counter(input().split(",")))

max_len = len(max(products.keys(), key=lambda x: len(x)))
print(max_len)

for key, value in sorted(products.items()):
    price = reduce(lambda x, y: ord(y) + x, key.replace(" ", ""), 0)
    print(key.ljust(max_len) + f": {price} UC x {value} = {price*value} UC")
