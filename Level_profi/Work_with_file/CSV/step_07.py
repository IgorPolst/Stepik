import csv
domen = {}
with open("Work_with_file/CSV/data.csv", "rt", encoding="UTF-8") as file: 
    for user in csv.DictReader(file, delimiter=","):
        user_email = user["email"]
        finde_domen = user_email[user_email.find("@")+1:]
        domen[finde_domen] = domen.get(finde_domen, 0) +1

sort_domen = dict(sorted(dict(sorted(domen.items())).items(), key = lambda el: el[1]))
domens = [[name_domen,count_domen] for name_domen, count_domen in sort_domen.items()]
columns = ["domain", "count"]

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)                 # запись заголовков
    for row in domens:                         # запись строк
        writer.writerow(row)


# Код 
# import csv

# domens = dict()

# with open('data.csv', encoding='utf-8') as f:
#     for *n,d in csv.reader(f):
#         key = d.split('@')[-1]
#         domens[key] = domens.get(key, 0) + 1
        
# del domens['email']

# with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['domain','count'])
#     for row in sorted(domens.items(), key=lambda x: (x[1], x[0])):
#         writer.writerow(row)