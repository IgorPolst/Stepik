from itertools import cycle, zip_longest

def roundrobin(*iterables):
    yield from (res for fresh in zip_longest(*iterables, fillvalue='')
        for res in fresh if res != '')



# INPUT DATA:

# TEST_1:
print(*roundrobin('abc', 'd', 'ef'))

# TEST_2:
numbers = [1, 2, 3]
letters = iter('beegeek')

print(*roundrobin(numbers, letters))

# TEST_3:
print(list(roundrobin()))

# TEST_4:
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = range(5)
letters = iter('beegeek')

print(*roundrobin(numbers1, numbers2, letters))

# TEST_5:
letters = iter('stepik')

print(*roundrobin(letters))

# TEST_6:
numbers = roundrobin(map(abs, range(-10, 10)))

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

# TEST_7:
numbers1 = map(abs, range(-10, 10))
numbers2 = filter(None, range(-10, 10))
numbers3 = map(abs, range(-5, 5))
numbers4 = filter(None, range(-5, 5))
numbers5 = map(abs, range(-1, 1))
numbers6 = filter(None, range(-1, 1))

print(*roundrobin(numbers1, numbers2, numbers3, numbers4, numbers5, numbers6))

# TEST_8:
print(list(roundrobin([], [], [], [])))

# TEST_9:
numbers = iter([1, 2, 3])
nones = iter([None, None, None, None])

print(*roundrobin(numbers, nones))