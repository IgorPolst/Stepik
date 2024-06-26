from datetime import timedelta, datetime

patern = "%d.%m.%Y"

start = datetime.strptime(input(), patern).date()
print(start.strftime(patern))
for i in range(1, 10):
    print((start + timedelta(days=1 + i)).strftime(patern))
    start += timedelta(days=1 + i)
