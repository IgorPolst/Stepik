from datetime import time, datetime, timedelta

time_work = {
    0: (time(9, 0), time(21, 0)),
    1: (time(9, 0), time(21, 0)),
    2: (time(9, 0), time(21, 0)),
    3: (time(9, 0), time(21, 0)),
    4: (time(9, 0), time(21, 0)),
    5: (time(10, 0), time(18, 0)),
    6: (time(10, 0), time(18, 0)),
}
now = datetime.strptime(input(), "%d.%m.%Y %H:%M")

if (
    time_work[now.weekday()][0] <= now.time()
    and time_work[now.weekday()][1] >= now.time()
):
    closing_time = datetime.combine(now.date(), time_work.get(now.weekday())[1])
    time_remaining = closing_time - now
    print(int(time_remaining.seconds // 60))
else:
    print("Магазин не работает")
