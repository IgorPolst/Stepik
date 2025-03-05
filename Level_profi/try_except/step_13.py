import calendar
import locale

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")


def get_weekday(number):
    if type(number) != int:
        raise TypeError("Аргумент не является целым числом")
    if number < 1 or number > 7:
        raise ValueError("Аргумент не принадлежит требуемому диапазону")
    return calendar.day_name[number - 1].title()


try:
    print(get_weekday("hello"))
except Exception as err:
    print(err)
    print(type(err))

try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))
