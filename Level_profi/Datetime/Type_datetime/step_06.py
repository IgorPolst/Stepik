from datetime import datetime as d
with open("diary.txt", "rt") as file:
    days = file.read().split("\n\n")


def convert_date(date) -> d:
    return d.strptime(date, "%d.%m.%Y; %H:%M\n") 

print(*sorted(days, key = lambda date: convert_date(date[:18])), sep = "\n\n")