from itertools import islice

def take(iterable, n):
    yield from islice(iterable, 0, n)
    


