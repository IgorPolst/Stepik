from itertools import tee, chain

def ncycles(iterable, times):
    return chain.from_iterable(tee(iterable, times))

# INPUT DATA:

# TEST_1:
print(*ncycles([1, 2, 3, 4], 3))

# TEST_2:
iterator = iter('bee')

print(*ncycles(iterator, 4))

# TEST_3:
iterator = iter([1])

print(*ncycles(iterator, 10))

# TEST_4:
iterator = ncycles(iter('b'), 1)

print(next(iterator))

# TEST_5:
iterator = ncycles(iter('g'), 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# TEST_6:
iterator = ncycles(iter([10, 10, 10, 10, 10]), 5)

print(*iterator)

# TEST_7:
print(list(ncycles([], 5)))