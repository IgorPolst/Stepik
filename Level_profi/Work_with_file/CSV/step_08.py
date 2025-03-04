import csv

conections = dict()
with open("Work_with_file/CSV/wifi.csv", "rt", encoding="UTF-8") as file:
    for region, area, *street, points in list(csv.reader(file, delimiter=";"))[1:]:
        conections[area] = conections.get(area, 0) + int(points)

for area, conect in sorted(
    dict(sorted(conections.items())).items(), key=lambda x: x[1], reverse=True
):
    print(f"{area}: {conect}")
