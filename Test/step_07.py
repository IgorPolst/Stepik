from datetime import datetime as dt

def is_available_date(booked_dates, date_for_booking):
    def convert_dates(dates):   
        available_date = []
        for date in dates:
            if "-" not in date:
                available_date.append(dt.strptime(date, "%d.%m.%Y"))
            else:
                start, end = date.split("-")
                for day in range(int(dt.timestamp(dt.strptime(start, "%d.%m.%Y"))), int(dt.timestamp(dt.strptime(end, "%d.%m.%Y")))+86400, 86400):
                    available_date.append(dt.fromtimestamp(day))
        return available_date

    booking = convert_dates(booked_dates)
    for_booking = convert_dates([date_for_booking])
    for check_date in for_booking:
        if check_date in booking:
            return False
    return True
   
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))
