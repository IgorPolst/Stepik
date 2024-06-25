def filter_anagrams(word, words):
    return list(filter(lambda new: sorted(word) == sorted(new), words))


word = "abba"
anagrams = ["aabb", "abcd", "bbaa", "dada"]
print(filter_anagrams("отсечка", ["сеточка", "стоечка", "тесачок", "чесотка"]))
