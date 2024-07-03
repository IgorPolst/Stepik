import calendar
from datetime import date, datetime

year = int(input())
month_list = []
for month in range(1, 13):
    count = 0
    for day in range (1, calendar.monthrange(year, month)[1]+1):
        if calendar.weekday(year, month, day) == 2:
            count += 1 
            if count == 3:
                month_list.append(date(year = year, month=month, day = day))
                break
print(*map(lambda dat: dat.strftime("%d.%m.%Y") ,month_list), sep = "\n")

