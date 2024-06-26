from datetime import date, time, datetime, timedelta
from functools import reduce
data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

time_works = list(map(lambda work: datetime.strptime(work[1], "%H:%M") - datetime.strptime(work[0], "%H:%M"),data))
print(int(reduce(lambda count, work:count + timedelta.total_seconds(work), time_works, 0)//60))
# print(timedelta.total_seconds(reduce(lambda work, count:timedelta(seconds=count) + datetime.strptime(work[1], "%H:%M") - datetime.strptime(work[0], "%H:%M"), data))//60)

