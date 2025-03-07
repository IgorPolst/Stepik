def my_pow(number):
    total = 0
    while number != 0:
        total += pow(number%10, len(number))
        number /=10
    return total