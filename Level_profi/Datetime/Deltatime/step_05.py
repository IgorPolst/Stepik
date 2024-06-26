from datetime import datetime, timedelta
patern = "%H:%M:%S"
alarm = datetime.strptime(input(), patern) + timedelta(seconds=int(input()))
print(alarm.strftime(patern))