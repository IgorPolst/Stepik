def around(iterable):
    it = iter(iterable)
    prev = None
    try:
        curr = next(it)
    except StopIteration:
        curr = None 

    while curr is not None:
        try:
            nxt = next(it)
        except StopIteration:
            nxt = None
        yield prev, curr, nxt
        prev, curr = curr, nxt

# INPUT DATA:

# TEST_1:
numbers = [1, 2, 3, 4, 5]

print(*around(numbers))

# TEST_2:
iterator = iter('hey')

print(*around(iterator))

# TEST_3:
iterator = around(iter('beegeek'))

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# TEST_4:
data = map(abs, range(-100, 100))

print(*around(data))

# TEST_5:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*around(data))

# TEST_6:
data = map(str.upper, 'y')

iterator = around(data)

print(next(iterator))

# TEST_7:
data = map(str.upper, 'yt')

print(*around(data))

# TEST_8:
data = map(str.upper, 'ytu')

print(*around(data))

# TEST_9:
data = ['bee', 'geek', 'stepik', 'python']

print(*around(data))

# TEST_10:
print(list(around([])))