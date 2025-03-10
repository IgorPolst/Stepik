def takes_positive(func):
    def wripper(*args, **kwargs):

        for i in args:
            if not isinstance(i, int):
                raise TypeError
            if i <= 0:
                raise ValueError
        for i in kwargs.values:
            if not isinstance(i, int):
                raise TypeError
            if i <= 0:
                raise ValueError
        return func(*args, **kwargs)

    return wripper
