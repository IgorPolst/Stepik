from datetime import datetime, timedelta

pattern = '%d.%m.%Y'

now = datetime.strptime(input(), pattern)
now_plus_7 = now + timedelta(days=7)
emp_dict = {}

for _ in range(int(input())):
    name, lname, date = input().split(' ')
    date = datetime.strptime(date, '%d.%m.%Y')
    if now < date.replace(year=now_plus_7.year) <= now_plus_7:
        emp_dict[name + ' ' + lname] = date
        
print('Дни рождения не планируются' if not emp_dict else max(emp_dict, key=emp_dict.get))
