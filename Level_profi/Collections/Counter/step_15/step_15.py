import csv, json
from collections import Counter, defaultdict
from functools import reduce


def file_reader(filename):
    count = defaultdict(int)
    with open(filename, "rt", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1].isdigit():
                count[row[0]] = int(row[1]) + int(row[2]) + int(row[3])
    return Counter(count)


with open(
    "Level_profi\Collections\Counter\step_15\prices.json", "rt", encoding="utf-8"
) as file:
    prices = dict(sorted(json.load(file).items()))

q1 = file_reader("Level_profi\Collections\Counter\step_15\quarter1.csv")
q2 = file_reader("Level_profi\Collections\Counter\step_15\quarter2.csv")
q3 = file_reader("Level_profi\Collections\Counter\step_15\quarter3.csv")
q4 = file_reader("Level_profi\Collections\Counter\step_15\quarter4.csv")

sales = q1 + q2 + q3 + q4
total = int()

for name, price in prices.items():
    total += sales[name] * price


print(total)
