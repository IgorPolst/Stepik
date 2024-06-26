from datetime import datetime, timedelta

now = datetime.strptime(input(), "%H:%M:%S").time()
print(int(timedelta.total_seconds(timedelta(hours=now.hour, minutes=now.minute, seconds=now.second))))
