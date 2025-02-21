import csv, json

with open("Stepik\Level_profi\Work_with_file\JSON\step_14\exam_results.csv",'rt', encoding="utf-8") as file:
    data = list(csv.DictReader(file))

best_score = []
for student in data:
    filtered = filter(lambda el: el["email"] == student["email"], data)
    best = sorted(filtered, key= lambda el: (el["score"], el["date_and_time"]), reverse=True)[0]
    list_best= list(best.items())
    list_best[2] = tuple(["best_score", int(list_best[2][1])]) 
    best = dict(list_best)

    flag = 1
    finde_element = dict()
    for el in best_score:
        if(el["email"] == best["email"]):
            flag = 0 
            finde_element = el
            break
    
    if flag : 
        best_score.append(best)

with open("Stepik/Level_profi/Work_with_file/JSON/step_14/best_scores.json",'wt', encoding="utf-8") as file:
    json.dump(sorted(best_score, key= lambda el: el["email"]), file, indent=1)