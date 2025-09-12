def pairwise(iterable):
    iterable = iter(iterable)
    old_el =  next(iterable)
    
    try:
        for el in iterable:
            yield old_el, el
            old_el = el
        old_el, el = el, None
        yield old_el, el 
    except:
        yield old_el, None

# Здоровое решение
def pairwise(iterable):
    it = iter(iterable)
    i = next(it, None)
    while i != None:
        i, prev = next(it, None), i
        yield prev, i
# INPUT DATA:

# TEST_1:
numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))

# TEST_2:
iterator = iter('stepik')

print(*pairwise(iterator))

# TEST_3:
print(list(pairwise([])))

# TEST_4:
data = map(abs, range(-100, 100))

print(*pairwise(data))

# TEST_5:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*pairwise(data))

# TEST_6:
data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

print(*pairwise(data))

# TEST_7:
iterator = pairwise('A')

print(next(iterator))

# TEST_8:
data = ['bee', 'geek', 'stepik', 'python']

print(*pairwise(data))