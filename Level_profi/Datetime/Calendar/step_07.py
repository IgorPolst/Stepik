import calendar
from datetime import date
def get_all_mondays(year):
    month_list = []
    for month in range(1, 13):
        for day in range (1, calendar.monthrange(year, month)[1]+1):
            if calendar.weekday(year, month, day) == 0:
                month_list.append(date(year = year, month=month, day = day))
    return month_list


print(get_all_mondays(2020))
