import functools


def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)

            return res + string if to_the_end else string + res

        return wrapper

    return decorator

@prefix('€')
def get_bonus():
    return '2000'
    
print(get_bonus())

@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'
       
print(get_bonus())