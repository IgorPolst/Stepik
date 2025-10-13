import calendar as c
from datetime import datetime

year, month = int(input()), int(input())

thursdays = []
_, num_days = c.monthrange(year, month)

for day in range(1, num_days + 1):
    if c.weekday(year, month, day) == c.THURSDAY:
        thursdays.append(day)

fourth_thursday = thursdays[3]

print(datetime(year, month, fourth_thursday).strftime("%d.%m.%Y"))