def is_prime(number):

    return number + 1 == sum(n for n in range(1, number + 1) if number % n == 0)
