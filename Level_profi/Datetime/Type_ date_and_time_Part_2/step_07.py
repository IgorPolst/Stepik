from datetime import date as d


def is_correct(day, month, year):
    try:
        d(year, month, day)
        return True
    except:
        return False


print(is_correct(31, 13, 2021))
