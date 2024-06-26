from datetime import datetime, timedelta

f = "%d.%m.%Y"
names_dates = [input() for _ in range(int(input()))]

birthdays = {}
for name in names_dates:
    birthday = datetime.strptime(name[-10:], f)
    birthdays[birthday] = birthdays.setdefault(birthday, [])
    birthdays[birthday].append(name[:-10].strip())
max_birthday = min(birthdays.items())
print(max_birthday[0].date().strftime(f), *max_birthday[1]) if len(max_birthday[1]) == 1 else print(max_birthday[0].date().strftime(f),len(max_birthday[1]))