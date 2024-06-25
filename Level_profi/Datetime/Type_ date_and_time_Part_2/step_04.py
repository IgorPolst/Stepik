from datetime import date

date = min([date.fromisoformat(input()) for _ in range(2)])
print(date.strftime("%d-%m (%Y)"))
