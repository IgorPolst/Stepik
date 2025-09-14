def first_largest(iterable, number):
    for i, x in enumerate(iterable):
        if x > number:
            return i
    return -1


#itertools

from itertools import compress, count

first_largest = lambda it, n: next(compress(count(), (i>n for i in it)), -1)