from itertools import dropwhile 
def drop_this(iterable, obj):
    yield from dropwhile(lambda x: x == obj, iterable)