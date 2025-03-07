def non_negative_even(numbers):
    new_numbers = filter(lambda number: number >= 0 and number % 2 == 0, numbers)
    return len(new_numbers) == numbers
