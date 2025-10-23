import functools

def recviz(func):
    depth = -1
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal depth
        depth += 1
        
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        all_args = ", ".join(args_repr + kwargs_repr)
        
        indent = "    " * depth
        print(f"{indent}-> {func.__name__}({all_args})")
        
        result = func(*args, **kwargs)
        
        print(f"{indent}<- {repr(result)}")
        
        depth -= 1
        return result
    
    return wrapper