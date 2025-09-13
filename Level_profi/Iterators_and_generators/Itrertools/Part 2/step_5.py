from itertools import compress
def take_nth(iterable, n):
    try:        
        return next(compress(iterable, [False for _ in range(n-1)] + [True]))
    except:
        return None
