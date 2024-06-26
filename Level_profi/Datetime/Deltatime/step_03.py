from datetime import datetime, timedelta

day = datetime.strptime(input(), "%d.%m.%Y")
print((day - timedelta(days=1)).strftime("%d.%m.%Y"))
print((day + timedelta(days=1)).strftime("%d.%m.%Y"))
