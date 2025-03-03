from collections import Counter

words = sorted(Counter(Counter(i).total() for i in input().split()).items(), key= lambda number: number[1])

for word in words:
    print(f"Слов длины {word[0]}: {word[1]}")
