import csv

humans = []  # Все люди бывшие на титанике
male = []
female = []

with open("Work_with_file/CSV/titanic.csv", "rt", encoding="UTF-8") as file:
    humans = list(csv.DictReader(file, delimiter=";"))


live_humans = filter(
    lambda live: live["survived"] == "1" and float(live["age"]) < 18, humans
)

for hum in live_humans:
    if hum["sex"] == "male":
        male.append(hum["name"])
    else:
        female.append(hum["name"])

print(*male, sep="\n")
print(*female, sep="\n")
