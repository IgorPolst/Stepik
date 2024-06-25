from datetime import date


def saturdays_between_two_dates(start, end):
    saturdays_count = 0
    if end < start:
        start, end = end, start
    for i in range(start.toordinal(), end.toordinal()):
        if date.weekday(date.fromordinal(i)) == 5:
            saturdays_count += 1
    return saturdays_count


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))
