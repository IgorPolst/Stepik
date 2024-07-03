import calendar

month = input().split()
print(calendar.month(int(month[0]), list(calendar.month_abbr).index(month[1])))
