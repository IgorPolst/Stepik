from datetime import timedelta, datetime

dates = [datetime.strptime(i, "%d.%m.%Y") for i in input().split()]
days_between = []
try: 
    for i in range (len(dates)-1):
        delta = (dates[i]-dates[i+1]).days
        days_between.append(delta) if dates[i] > dates[i+1] else days_between.append(-delta)
    print(days_between)
except:
    print(days_between)
        
# Здоровое решение!
# from datetime import date, time, timedelta, datetime

# dates = [datetime.strptime(dt, '%d.%m.%Y') for dt in input().split()]

# diffs = [abs(dates[i] - dates[i-1]).days for i in range(1, len(dates))]
    
# print(diffs)