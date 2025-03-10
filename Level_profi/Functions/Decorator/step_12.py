import functools


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                res = func(*args, **kwargs)
            return res

        return wrapper

    return decorator


@repeat(3)
def say_beegeek():
    """documentation"""
    print("beegeek")


say_beegeek()


@repeat(4)
def say_beegeek():
    """documentation"""
    print("beegeek")


print(say_beegeek.__name__)
print(say_beegeek.__doc__)
