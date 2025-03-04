import json
from datetime import datetime, timedelta


def count_time(pool):
    start, finish = pool["WorkingHoursSummer"]["Понедельник"].split("-")
    start = datetime.strptime(start, "%H:%M")
    finish = datetime.strptime(finish, "%H:%M")
    return pool["WorkingHoursSummer"]["Понедельник"][
        :5
    ] == "10:00" and finish - start >= timedelta(hours=2)


with open(
    "Stepik\Level_profi\Work_with_file\JSON\step_13\pools.json", "rt", encoding="utf-8"
) as file:
    data = filter(lambda pool: count_time(pool), json.load(file))
data = sorted(
    data,
    key=lambda pool: (
        pool["DimensionsSummer"]["Length"],
        pool["DimensionsSummer"]["Width"],
    ),
    reverse=True,
)[0]


print(
    f"{data['DimensionsSummer']['Length']}x{data['DimensionsSummer']['Width']}\n{data['Address']}"
)
