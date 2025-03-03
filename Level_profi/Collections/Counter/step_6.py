from collections import Counter

fructs = Counter(input().lower().split()).most_common()

print(fructs[0][0])