import functools


def returns(datetype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if not isinstance(res, datetype):
                raise TypeError

            return res

        return wrapper

    return decorator


@returns(int)
def add(a, b):
    return a + b


print(add(10, 5))


@returns(int)
def add(a, b):
    return a + b


try:
    print(add("199", "1"))
except TypeError as e:
    print(type(e))


@returns(list)
def beegeek():
    """beegeek docs"""
    return "beegeek"


print(beegeek.__name__)
print(beegeek.__doc__)

try:
    print(beegeek())
except TypeError as e:
    print(type(e))
