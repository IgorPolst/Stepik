import csv
from collections import namedtuple
from datetime import datetime

Friend = namedtuple("Friend", "surname,name,meeting_date,meeting_time")

with open("Level_profi/Collections/NamedTuple/step_5/meetings.csv", "rt", encoding = "utf-8") as file: 
    friends = list(map(lambda friend: Friend(*friend.values()) ,csv.DictReader(file, delimiter=",")))

friends = sorted(friends, key = lambda f:(datetime.strptime(f.meeting_date, "%d.%m.%Y"), datetime.strptime(f.meeting_time, "%H:%M")))

for friend in friends:
    print(f"{friend.surname} {friend.name}")