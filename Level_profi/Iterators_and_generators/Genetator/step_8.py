def flatten(nested_list):
    for elem in nested_list:
        if type(elem) == list:
            yield from flatten(elem)
        else:
            yield elem


generator = flatten([1, 2, 3, 4, 5, 6, 7])

print(*generator)

generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)
