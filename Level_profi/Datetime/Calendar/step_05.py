import calendar

year, month = [i for i in input().split()]
month_number = list(calendar.month_name).index(month)

print(calendar.monthrange(int(year), month_number))