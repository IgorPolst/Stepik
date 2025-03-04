import csv

with open(
    "Stepik/Level_profi/Work_with_file/CSV/student_counts.csv", "rt", encoding="utf-8"
) as file:
    data = list(csv.DictReader(file))
    field = list(data[0].keys())

fieldnames = [field[0]] + sorted(field[1:], key=lambda x: (int(x.split("-")[0]), x[2]))
print(*fieldnames)

with open(
    "Stepik/Level_profi/Work_with_file/CSV/sorted_student_counts.csv",
    "w",
    newline="",
    encoding="utf-8",
) as file:
    result = csv.DictWriter(file, fieldnames=fieldnames)

    result.writeheader()
    result.writerows(data)
