import json

with open(
    "Level_profi/Work_with_file/JSON/step_15/food_services.json", "rt", encoding="utf-8"
) as file:
    data = json.load(file)


popular_region = {}
popular_company = {}
for cafe in data:
    popular_region[cafe["District"]] = (
        popular_region.setdefault(cafe["District"], 0) + 1
    )
    popular_company[cafe["OperatingCompany"]] = (
        popular_company.setdefault(cafe["OperatingCompany"], 0) + 1
    )

most_popular_region = max(popular_region.items(), key=lambda region: region[1])
most_popular_company = max(
    (company for company in popular_company.items() if company[0] != ""),
    key=lambda company: company[1],
)
print(f"{most_popular_region[0]}: {most_popular_region[1]}")
print(f"{most_popular_company[0]}: {most_popular_company[1]}")
