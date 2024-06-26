from datetime import datetime, timedelta, date

week_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
now = datetime(1, 1, 1)
while now < datetime(9999, 12, 31):
    if now.day != 13:
        now += timedelta(days=1)
        continue
    check = (now.date()).weekday()
    week_dict[check] = week_dict.get(check) + 1
    now += timedelta(days=1)
print(*week_dict.values(), sep="\n")
