def starmap(func, iterable):
    return map(lambda el: func(*el), iterable)


# TEST_1:
pairs = [(1, 3), (2, 5), (6, 4)]

print(*starmap(lambda a, b: a + b, pairs))

# TEST_2:
points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]

print(*starmap(lambda x, y, z: x * y * z, points))

# TEST_3:
points = [(1, 1, 1, 0), (1, 1, 2, 0), (2, 2, 3, 10)]

print(*starmap(lambda x, y, z, t: x + y + z + t, points))

# TEST_4:
points = [[10], [-9], [2]]

print(*starmap(lambda x: x**2, points))

# TEST_5:
points = [
    (1, 1, 1, 0, 90),
    (1, 1, 2, 0, 67),
    (2, 2, 3, 10, -56),
    (5, 21, 3, 10, -56),
    (6, 24, 35, 100, 36),
    (8, 34, 3, 10, 56),
]

print(*starmap(lambda x, y, z, t, w: x + y * z + t + w**6, points))
