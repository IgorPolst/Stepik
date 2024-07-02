import time
def calculate_it (func, *args):
    start_time = time.perf_counter() 
    result = func(*args)
    end_time = time.perf_counter()
    return tuple([result, end_time-start_time])

