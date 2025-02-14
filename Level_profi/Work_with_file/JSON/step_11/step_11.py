import csv, json

with open('Stepik/Level_profi/Work_with_file/JSON/step_11/playgrounds.csv','rt', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter=";"))

playgroundes = dict()
for playground in data[1:]:

    playgroundes.setdefault(playground[1],{}).setdefault(playground[2], []).append(playground[3])
print(playgroundes)

with open('Stepik/Level_profi/Work_with_file/JSON/step_11/addresses.json', 'wt', encoding="utf-8") as file:
    json.dump(playgroundes, file, indent = 3,ensure_ascii= False)