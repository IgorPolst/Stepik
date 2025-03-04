import calendar

try:
    number_month = int(input())
    if number_month <= 0:
        raise IndexError
    name_month = calendar.month_name[number_month]
    print(name_month)
except ValueError:
    print("Введено некорректное значение")
except IndexError:
    print("Введено число из недопустимого диапазона")
