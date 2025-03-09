new_print = print

def print(*args , sep=" ", end = "\n"):

    args = map(lambda el: el.upper() if isinstance(el, str) else el, args)
    new_print(*args, sep=sep.upper(), end = end.upper())

print('beegeek', [1, 2, 3], 4)