import random


def random_numbers(left: int, right: int):
    res = iter([random.randint(left, right) for _ in range(left, right)])
    return res


iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))


iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
