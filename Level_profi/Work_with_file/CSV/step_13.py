import csv

with open(
    "Stepik/Level_profi/Work_with_file/CSV/prices.csv", "rt", encoding="utf-8"
) as file:
    data = list(csv.DictReader(file, delimiter=";"))

best_product = {"shop": "", "product": "", "price": 1000}

for shop in data:
    for price in list(shop.values())[1:]:
        if int(best_product["price"]) >= int(price):
            best_product["price"] = int(price)
            best_product["shop"] = shop["Магазин"]
            best_product["product"] = list(shop.keys())[
                list(shop.values()).index(price)
            ]
print(best_product["product"].strip(), ": ", best_product["shop"], sep="")
