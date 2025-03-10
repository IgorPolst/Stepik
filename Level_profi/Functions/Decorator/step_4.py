def reverse_args(func):
    def wripper(*args, **kwargs):
        args = args[::-1]
        return func(*args, **kwargs)

    return wripper
