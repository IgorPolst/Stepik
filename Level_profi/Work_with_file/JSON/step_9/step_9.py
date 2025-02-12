import json
from functools import reduce

with open("Stepik\Level_profi\Work_with_file\JSON\step_9\people.json", "rt", encoding="utf-8") as file:
    data = json.loads(file.read())
 
all_key = {key : None for key in reduce(lambda x1, x2: x1 | x2, data, {})}
result_data = [all_key | people for people in data]

with open("Stepik/Level_profi/Work_with_file/JSON/step_9/updated_people.json", "wt", encoding="utf-8") as file:
    json.dump(result_data, file)