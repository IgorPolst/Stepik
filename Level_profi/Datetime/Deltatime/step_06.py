from datetime import datetime


def num_of_sundays(year):
    return (datetime(year=int(year), month=12, day=31).date()).strftime("%U")


print(num_of_sundays(2023))
