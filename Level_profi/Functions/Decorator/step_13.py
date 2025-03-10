import functools


def strip_range(start, end, char="."):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)

            res = "".join(
                [char if i >= start and i < end else res[i] for i in range(len(res))]
            )

            return res

        return wrapper

    return decorator


@strip_range(3, 5)
def beegeek():
    return "beegeek"


print(beegeek())


@strip_range(3, 20, "_")
def beegeek():
    return "beegeek"


print(beegeek())


@strip_range(20, 30)
def beegeek():
    return "beegeek"


print(beegeek())
