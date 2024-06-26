from datetime import timedelta, datetime


def fill_up_missing_dates(dates):
    patrn = "%d.%m.%Y"
    dates = sorted(list(map(lambda date: datetime.strptime(date, patrn).date(), dates)))
    new_dates, chek_date = [], dates[0]
    while chek_date <= dates[len(dates) - 1]:
        new_dates.append(chek_date.strftime(patrn))
        chek_date += timedelta(days=1)
    return new_dates


dates = ["01.11.2021", "07.11.2021", "04.11.2021", "03.11.2021"]

print(fill_up_missing_dates(dates))

# # По проще

# def fill_up_missing_dates(dates):
#     pattern = '%d.%m.%Y'
#     dates = [datetime.strptime(d, pattern) for d in dates]
#     start, end = min(dates), max(dates)
#     days = (end - start).days
#     return [(start + timedelta(days=i)).strftime(pattern) for i in range(days + 1)]
