from datetime import datetime


birthdays = {}

for _ in range(int(input())):
    *names, birth_date = input().split()
    birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()
    if birth_date in birthdays:
        birthdays[birth_date] += 1
    else:
        birthdays[birth_date] = 1

max_count = max(birthdays.values())
most_common_dates = list(filter(lambda data: data[1] == max_count,birthdays.items()))

print(*most_common_dates, sep = "\n")