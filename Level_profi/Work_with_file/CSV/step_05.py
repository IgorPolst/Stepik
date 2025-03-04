import csv

column = int(input())
with open("Work_with_file/CSV/deniro.csv", "rt", encoding="UTF-8") as file:
    rows = list(csv.reader(file, delimiter=","))
for row in sorted(
    rows,
    key=lambda row: (
        int(row[column - 1]) if row[column - 1].isdigit() else row[column - 1]
    ),
):
    print(f"{row[0]},{row[1]},{row[2]}")
