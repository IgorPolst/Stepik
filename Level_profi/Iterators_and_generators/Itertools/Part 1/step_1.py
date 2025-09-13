from itertools import count, starmap

def tabulate(func):
    yield from (func(num) for num in count(1))

func = lambda x: x
values = tabulate(func)

print(values)
print(next(values))
print(next(values))