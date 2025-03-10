import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f"TRACE: вызов {func.__name__}() с аргументами: {tuple(args)}, {kwargs}")
        answer = "'"+res+"'" if isinstance(res,str) else res
        print(
            f"TRACE: возвращаемое значение {func.__name__}(): {answer}"
        )
        return res

    return wrapper


@trace
def say(name, line):
    return f"{name}: {line}"


say("Jane", "Hello, World")

@trace
def sub(a, b, c):
    '''прекрасная функция'''
    return a - b + c
    
print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)