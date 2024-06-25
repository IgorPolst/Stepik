def mean(*args):
    sum = 0
    kol = 0
    for i in args: 
        if type(i) is int or type(i) is float:
            sum += i
            kol += 1
    if sum == 0:
        kol = 1
    return sum/kol

print(mean(True, ['stepik'], 'beegeek', (1, 2)))