def get_max_index(numbers):
    max_index = len(numbers) - 1
    max_value = numbers[0]

    for index, value in enumerate(numbers, 0):
        if value > max_value:
            max_index = index
            max_value = value

    return max_index
