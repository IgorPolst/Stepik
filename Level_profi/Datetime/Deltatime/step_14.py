from datetime import datetime, timedelta

f = "%d.%m.%Y"
start, end = [datetime.strptime(input(), f) for _ in "__"]

while (int(start.day) + int(start.month)) % 2 != 1:
    start += timedelta(days=1)

while start <= end:
    if start.weekday() not in [0, 3]:
        print(start.strftime(f))
    start += timedelta(days=3)
