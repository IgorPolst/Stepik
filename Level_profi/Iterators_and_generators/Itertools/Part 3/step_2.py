from itertools import pairwise

def is_rising(iterable):
    return all(map(lambda a: a[0] < a[1], pairwise(iterable)))

# INPUT DATA:

# TEST_1:
print(is_rising([1, 2, 3, 4, 5]))

# TEST_2:
iterator = iter([1, 1, 1, 2, 3, 4])

print(is_rising(iterator))

# TEST_3:
iterator = iter(list(range(100, 200)))

print(is_rising(iterator))

# TEST_4:
iterator = iter(list(range(200, 100, -1)))

print(is_rising(iterator))

# TEST_5:
iterator = iter(list(range(100, 201)) + [200])

print(is_rising(iterator))

# TEST_6:
iterator = iter([10]*50)

print(is_rising(iterator))