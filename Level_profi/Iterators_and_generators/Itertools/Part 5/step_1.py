from itertools import permutations

print(*sorted(set(["".join(word) for word in permutations([i for i in input()])])), sep="\n")

