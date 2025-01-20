import csv


unik = dict()
with open("Work_with_file/CSV/name_log.csv", "rt", encoding="UTF-8") as file:
    new_name = sorted(csv.DictReader(file, delimiter=","), key = lambda email: email["dtime"], reverse= True)

for name in new_name:
    unik[name["email"]] = unik.setdefault(name["email"], [])
    unik[name["email"]].append(name)

    

print(*unik.values(), sep = "\n")