def print_digits(number):
    if number > 0:
        print_digits(number//10)
        print(number%10)