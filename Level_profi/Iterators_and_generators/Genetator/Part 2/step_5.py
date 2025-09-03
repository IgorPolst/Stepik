def interleave(*args):

    return (el for elem in zip(*args) for el in elem)


print(*interleave("bee", "123"))
