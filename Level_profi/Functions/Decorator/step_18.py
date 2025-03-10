import functools


class MaxRetriesException(Exception):
    pass


def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == times - 1:
                        raise MaxRetriesException(
                            "Maximum retry attempts exceeded"
                        ) from e
            raise MaxRetriesException

        return wrapper

    return decorator


@retry(3)
def no_way():
    raise ValueError


try:
    no_way()
except Exception as e:
    print(type(e))


@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get("calls", 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print("beegeek")


beegeek()
