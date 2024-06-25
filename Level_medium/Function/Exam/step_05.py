from functools import reduce
def product_of_odds(data):  # data - список целых чисел
    return reduce(lambda result, i:result*i ,filter(lambda i: i%2 == 1, data), 1)
