from collections import Counter


def count_occurences(word, words):
    word = word.lower()
    words = words.lower()

    counter = Counter(words.split())
    return counter[word]


word = "python"
words = "Python Conferences python training python events"

print(count_occurences(word, words))
