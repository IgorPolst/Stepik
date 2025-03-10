from collections import deque


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    d = deque(numbers)
    d.rotate(step)
    for i in range(len(numbers)):
        numbers[i] = d[i]
    return None


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)

print(numbers)
