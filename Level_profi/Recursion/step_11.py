def number_of_frogs(year):
    if year == 1:
        return 77
    return 3 * (number_of_frogs(year - 1) - 30)

print(number_of_frogs(int(input())))
