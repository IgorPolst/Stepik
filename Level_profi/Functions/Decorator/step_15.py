import functools


def takes(*arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if all(map(lambda el: isinstance(el, arg), [*args, *kwargs.values()])):
                res = func(*args, **kwargs)
                return res
            else:
                raise TypeError

        return wrapper

    return decorator


@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times


try:
    print(repeat_string("bee", 4))
except TypeError as e:
    print(type(e))


@takes(int, str)
def repeat_string(string, times):
    return string * times


print(repeat_string("bee", 3))
