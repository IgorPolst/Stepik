import time
def get_the_fastest_func(funcs, arg):
    best_time = 1000

    for func in funcs: 
        start_time = time.perf_counter()
        func(arg)
        end_time = time.perf_counter()
        work_time = end_time - start_time
        if best_time > work_time:
            best_time = work_time
            best_func = func        
    return best_func