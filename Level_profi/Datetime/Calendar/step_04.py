import calendar
year, month = [int(i) for i in input().split()] 
print(calendar.monthrange(year, month)[1])