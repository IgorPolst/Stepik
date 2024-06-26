from datetime import timedelta, datetime

patern = "%H:%M"
end_of_lesson = datetime.strptime(input(), patern) + timedelta(minutes=45)
end_of_work = datetime.strptime(input(), patern)
while end_of_lesson <= end_of_work:
    end_of_lesson += timedelta(minutes=10)
    start_of_lesson = end_of_lesson - timedelta(minutes=55)
    print(
        f"{start_of_lesson.strftime(patern)} - {(end_of_lesson-timedelta(minutes=10)).strftime(patern)}"
    )
    end_of_lesson += timedelta(minutes=45)

# Разумный вариант решения
# from datetime import datetime, timedelta
# f = '%H:%M'
# start, stop = (datetime.strptime(input(), f) for i in '__')
# while start <= (stop - timedelta(minutes=45)):
#     print(start.strftime(f), '-', (start + timedelta(minutes=45)).strftime(f))
#     start += timedelta(minutes=55)
