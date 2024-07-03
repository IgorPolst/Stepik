def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


import time


def calculate_it(func):
    start_time = time.perf_counter()
    result = func(range(100000))
    end_time = time.perf_counter()
    print(end_time - start_time)


calculate_it(list_comprehension)
calculate_it(for_and_append)
calculate_it(list_function)
