from itertools import groupby

def ranges(numbers):
    sort_numbers = groupby(numbers, key=lambda num: numbers.index(num) - num)
    res = []
    for _, numberes in sort_numbers:
        new_numbers = [*numberes]
        res += [tuple([new_numbers[0], new_numbers[-1]])]

    return res
         


numbers = [1, 2, 3, 4, 7, 8, 10]
# ranges(numbers)
print(ranges(numbers))