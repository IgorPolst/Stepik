from collections import Counter

products = Counter(input().split(","))

for key, value in sorted(products.items()):
    print(f"{key}: {value}")