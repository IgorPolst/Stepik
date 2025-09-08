import calendar
from datetime import *

def years_days(year: int):
    start_ordinal = date(year, 1, 1).toordinal()
    days_in_year = 366 if calendar.isleap(year) else 365
    end_ordinal = start_ordinal + days_in_year
    for ordinal in range(start_ordinal, end_ordinal):
        yield date.fromordinal(ordinal)

# TEST_1:
dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))

# TEST_2:
dates = years_days(2077)

print(*dates)

# TEST_3:
dates = years_days(2000)

print(*dates)

# TEST_4:
dates = years_days(1900)

print(*dates)