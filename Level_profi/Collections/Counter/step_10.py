from collections import Counter

c = Counter({i: int(j) for i, j in (s.split() for s in open(0))})
print(c.most_common()[-2][0])
