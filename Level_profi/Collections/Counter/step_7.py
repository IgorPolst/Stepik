from collections import Counter

fructs = Counter(input().lower().split())
rare_fructs = filter(lambda fruct: fruct[1] == min(fructs.values()), fructs.items())

print(", ".join(sorted([i[0] for i in rare_fructs])))
