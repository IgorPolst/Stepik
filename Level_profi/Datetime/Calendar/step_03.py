from datetime import datetime
import calendar
today = datetime.strptime(input(), "%Y-%m-%d")
print(calendar.day_name[today.weekday()])

