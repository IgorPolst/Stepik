from functools import lru_cache
import sys


@lru_cache
def sorted_words(text):
    return "".join(sorted([i for i in text]))


for word in [i.strip() for i in sys.stdin]:
    print(sorted_words(word))
