def print_given(*args, **kwargs):
    for arg in args:
        print(f"{arg} {type(arg)}")
    kwargs = dict(sorted(kwargs.items()))
    for kwarg_key, kwarg_value in kwargs.items():
        print(f"{kwarg_key} {kwarg_value} {type(kwarg_value)}")


print_given("apple", "cherry", "watermelon")
