import string 
from itertools import cycle

def alnum_sequence():
    letters = cycle(string.ascii_uppercase)
    numbers = cycle(range(1,27))
    while True:
        yield next(numbers)
        yield next(letters)

alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))

