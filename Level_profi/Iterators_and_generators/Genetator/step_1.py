def simple_sequence():
    el = 1
    while True:
        for _ in range(el):
            yield el
        el += 1


generator = simple_sequence()

print(next(generator))
print(next(generator))
