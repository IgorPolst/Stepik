from math import factorial                   # функция из модуля math     


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)    


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

import time
def calculate_it (func, arg = 900):
    start_time = time.perf_counter() 
    result = func(arg)
    end_time = time.perf_counter()
    print(end_time-start_time)


calculate_it(factorial)
calculate_it(factorial_classic)
calculate_it(factorial_recurrent)
