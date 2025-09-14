from itertools import chain
def sum_of_digits(iterable):
    return sum(map(lambda x: int(x), chain.from_iterable(map(lambda x: str(x), iterable))))

# INPUT DATA:

# TEST_1:
print(sum_of_digits([13, 20, 41, 2, 2, 5]))

# TEST_2:
print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

# TEST_3:
print(sum_of_digits([123456789]))

# TEST_4:
numbers = [10]*100

iterator = iter(numbers)
print(sum_of_digits(iterator))

# TEST_5:
numbers = [100, 20, 30, 400, 500, 5]*100000

print(sum_of_digits(numbers))