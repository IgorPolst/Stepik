import csv


unik = dict()
with open(
    "Stepik/Level_profi/Work_with_file/CSV/name_log.csv", "rt", encoding="UTF-8"
) as file:
    new_name = sorted(
        csv.DictReader(file, delimiter=","),
        key=lambda email: email["dtime"],
        reverse=True,
    )

for name in new_name:
    unik[name["email"]] = unik.setdefault(name["email"], [])
    unik[name["email"]].append(name)

new_unik = list(
    sorted(
        (map(lambda people: people[0], unik.values())),
        key=lambda email: email["email"],
    )
)


with open(
    "Stepik/Level_profi/Work_with_file/CSV/new_name_log.csv", "wt", encoding="UTF-8"
) as file:
    write = csv.DictWriter(file, new_unik[0].keys(), delimiter=",", lineterminator="\n")
    write.writeheader()
    write.writerows(new_unik)
