def get_min_max(iterable):
    iterable = iter(iterable)

    try:
        minim = next(iterable)
        maxim = minim
        for i in iterable:
            minim = i if i < minim else minim
            maxim = i if i > maxim else maxim
        return tuple([minim, maxim])
    except:
        return None


# INPUT DATA:

# TEST_1:
iterable = iter(range(10))

print(get_min_max(iterable))

# TEST_2:
iterable = [6, 4, 2, 33, 19, 1]

print(get_min_max(iterable))

# TEST_3:
iterable = iter([])

print(get_min_max(iterable))

# TEST_4:
data = iter((9, 9, 9, 9, 9))

print(get_min_max(data))

# TEST_5:
data = iter(range(1, 101))

print(get_min_max(data))

# TEST_6:
data = list(range(1, 101))[::-1]

print(get_min_max(data))

# TEST_7:
data = iter(
    [
        -86,
        -51,
        33,
        -23,
        40,
        96,
        19,
        -65,
        26,
        12,
        -93,
        68,
        82,
        47,
        -58,
        -37,
        -100,
        5,
        75,
        54,
        -79,
        -72,
        -2,
        61,
        -16,
        -9,
        89,
        -44,
        -30,
    ]
)

print(get_min_max(data))

# TEST_8:
data = iter(
    [
        -86,
        -51,
        33,
        -23,
        40,
        96,
        19,
        -65,
        26,
        12,
        -93,
        68,
        82,
        47,
        -58,
        -37,
        -100,
        5,
        75,
        54,
        -79,
        -72,
        -2,
        61,
        -16,
        -9,
        89,
        -44,
        -30,
        -100,
        96,
        -100,
        1,
        2,
        -99,
        96,
    ]
)

print(get_min_max(data))

# TEST_9:
iterable = []

print(get_min_max(iterable))

# TEST_10:
iterable = [69]

print(get_min_max(iterable))

# TEST_11:
data = iter(range(100_000_000))

print(get_min_max(data))

# TEST_12:
data = iter(["a", "b", "c", "aaa", "abc", "cbc", "bbb"])

print(get_min_max(data))

# TEST_13:
data = iter(["bbb"])

print(get_min_max(data))
