def recursive_sum(a, b):
    if a == 0 and b == 0:
        return 0
    else:
        if a > b:
            return 1 + recursive_sum(a - 1, b)
        else:
            return 1 + recursive_sum(a, b - 1)
