from collections import Counter

fructs = Counter(input().lower().split())
rare_fructs = filter(lambda fruct: fruct[1] == max(fructs.values()), fructs.items())

print(sorted([i[0] for i in rare_fructs], reverse=True)[0])
