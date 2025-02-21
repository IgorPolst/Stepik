import json

with open("Stepik/Level_profi/Work_with_file/JSON/step_15/food_services.json",'rt', encoding="utf-8") as file:
    data =  json.load(file)

poular_region = {}
