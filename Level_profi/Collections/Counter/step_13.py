from collections import Counter

def scrabble(symbols, word):
    symbols = Counter(symbols.lower())
    word = Counter(word.lower())

    return symbols & word == word



print(scrabble('eeeeegggggggeeeeeekkkkk', 'Beegeek'))