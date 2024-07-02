from datetime import datetime, timedelta

f = "%d.%m.%Y"
present_time = datetime(2022,11,8,12,00)
today = datetime.today().isoformat()
print(today, present_time)