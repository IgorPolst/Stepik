def get_days_in_month(year, month):
    import calendar
    from datetime import date
    month_number = list(calendar.month_name).index(month)       
    days_in_month = calendar.monthrange(int(year), month_number)[1]
    return [date(day=day, month=month_number, year=year) for day in range(1, days_in_month+1)] 

print(get_days_in_month(2021, 'December'))