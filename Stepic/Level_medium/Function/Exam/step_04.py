from functools import reduce


def concat(*words, sep=" "):
    return reduce(lambda stri, word: stri + sep +str(word), words, "")[len(sep):]

print(concat ('hello', 'python', 'and', 'stepik', sep = "()"))
