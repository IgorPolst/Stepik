from datetime import date


def print_good_dates(dates):
    dates = filter(
        lambda date: date.year == 1992 and date.month + date.day == 29, dates
    )
    print(*map(lambda date: date.strftime("%B %d, %Y"), sorted(dates)), sep="\n")


dates = [date(1992, 9, 20), date(1992, 8, 21), date(1992, 7, 22), date(1992, 10, 19)]
print_good_dates(dates)
