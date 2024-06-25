# from datetime import datetime as d
# def  is_available_date(booked_dates, date_for_booking):
#     booked = convert_dates(booked_dates) 
#     booking = convert_dates([date_for_booking])
#     print(booked)
#     print(booking)
#     for i in booking:
#         if i not in booked:
#             return False
#     return True
   

# def convert_dates(dates):   
#     available_date = []
#     for date in dates:
#         if  len(date) == 10:
#             available_date.append(d.strptime(date, "%d.%m.%Y"))
#         else: 
#             start, end = date.split("-")
            
#             for day in range(int(d.timestamp(d.strptime(start, "%d.%m.%Y"))), int(d.timestamp(d.strptime(end, "%d.%m.%Y")))+int(d.timestamp(d(0,0,1)))) :
#                 available_date.append(d.fromtimestamp(day))       
#     return available_date

# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021'
# print(int(d.timestamp(d(1970,1,1))))
# print(is_available_date(dates, some_date))


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
    print(booking)
    print(for_booking)
    for check_date in for_booking:
        if check_date not in booking:
            return False
    return True
   
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))
