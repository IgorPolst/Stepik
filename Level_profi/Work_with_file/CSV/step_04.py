import csv
companies = {}
with open("Work_with_file/CSV/salary_data.csv", "rt", encoding="UTF-8") as file: 
    for company in csv.DictReader(file, delimiter=";"): 
        companies [company["company_name"]] = companies.setdefault(company["company_name"], [])
        companies[company["company_name"]].append(int(company["salary"]))
sorted_companies = dict(
    sorted(
        dict(
            sorted(companies.items())).items(), key = lambda company: sum(company[1])//len(company[1])
        )
    ).keys() 

print(*sorted_companies, sep = "\n")
