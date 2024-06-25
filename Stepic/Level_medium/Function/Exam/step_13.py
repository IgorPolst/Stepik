from functools import reduce
words = []


def geometria(word):
    return sum(map(lambda el: ord(str(el).upper() - ord("A"), word), 0))


for _ in range(int(input())):
    word = input()
    words.append([geometria(word), word])
print(
    *map(lambda word: word[1], sorted(sorted(words, key=lambda word: word[1]))),
    sep="\n"
)
