number = int(input())

if number < 0 or number > 36:
    print("ошибка ввода")
elif number == 0:
    print("зеленый")
elif number <= 10:
    if number % 2 == 0:
        print("черный")
    else:
        print("красный")
elif number <= 18:
    if number % 2 == 1:
        print("черный")
    else:
        print("красный")
elif number <= 28:
    if number % 2 == 0:
        print("черный")
    else:
        print("красный")
elif number <= 36:
    if number % 2 == 1:
        print("черный")
    else:
        print("красный")
