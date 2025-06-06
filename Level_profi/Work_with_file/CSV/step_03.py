import csv

with open(
    "Stepik\Level_profi\Work_with_file\CSV\sales.csv", "rt", encoding="UTF-8"
) as file:
    sales = list(csv.reader(file, delimiter=";"))
    print(
        *list(
            map(
                lambda name: name[0],
                filter(lambda sale: int(sale[2]) < int(sale[1]), sales[1:]),
            )
        ),
        sep="\n"
    )
