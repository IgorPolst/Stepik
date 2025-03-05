def to_100(number):
    if number <= 100:
        print(number)
        to_100(number + 1)


to_100(1)
