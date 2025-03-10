def upper_case_print(func):
    def wrapper(*args, **kwargs):
        modified_args = [str(arg).upper() for arg in args]  
        modified_kwargs = {k: str(v).upper() for k, v in kwargs.items()}      
        return func(*modified_args, **modified_kwargs)
    
    return wrapper

print = upper_case_print(print)