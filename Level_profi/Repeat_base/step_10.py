def choose_plural(amount, declensions):
    if amount % 10 in [0, 5, 6, 7, 8, 9] or amount % 100 in [11, 12, 13, 14]:
        koin = 2
    elif amount % 10 == 1:
        koin = 0
    elif amount % 10 in [2, 3, 4]:
        koin = 1

    return f"{amount} {declensions[koin]}"


print(choose_plural(8, ("яблоко", "яблока", "яблок")))
