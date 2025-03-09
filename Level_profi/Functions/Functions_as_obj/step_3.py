def polynom(x):
    res = pow(x, 2) + 1
    polynom.values.add(res)
    return res


polynom.values = set()
