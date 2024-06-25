def same_parity(numbers):
    return list(filter(lambda num: numbers[0] % 2 == num % 2, numbers))


print(same_parity([-7, 0, 67, -9, 70, -29, 90]))
