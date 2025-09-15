from itertools import groupby

def group_anagrams(words):
    words_groped = groupby(sorted(words, key=sorted), key=sorted)
    yield from (tuple(words[1]) for words in words_groped)


groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])

print(*groups, sep="\n")