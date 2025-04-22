def alternating_sequence(count=None):
    num = 1  # начинаем с 1

    if count is None:
        while True:
            yield num
            num = -num - 1 if num > 0 else -num + 1
    else:
        for _ in range(count):
            yield num
            num = -num - 1 if num > 0 else -num + 1



generator = alternating_sequence()

print(next(generator))
print(next(generator))

generator = alternating_sequence(10)

print(*generator)