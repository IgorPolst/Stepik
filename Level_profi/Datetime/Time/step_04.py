def for_and_append():                            # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result
        

def list_comprehension():                        # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)] 

import time
def calculate_it (func, arg = 900):
    start_time = time.perf_counter() 
    list = func()
    end_time = time.perf_counter()
    print(end_time-start_time)


calculate_it(list_comprehension())
calculate_it(for_and_append())
