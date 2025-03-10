def do_twice(func):
    def wripper(*args, **kwargs):
        return func(args, kwargs) * 2

    return wripper
