import json

with open('Stepik/Level_profi/Work_with_file/JSON/step_7/data7.json', 'rt', encoding='utf-8') as file:
    data = json.load(file)


new_data = list()
for object in data:
 
    if(isinstance(object, str)):
        object += "!"
    elif(isinstance(object, bool)):
        object = not object
    elif(isinstance(object, int) or isinstance(object, float)):
        object += 1
    elif(isinstance(object, list)):
        object *= 2
    elif(isinstance(object, dict)):
        object = object | {"newkey": None}

    if(object != None): 
        new_data.append(object)  

with open('Stepik/Level_profi/Work_with_file/JSON/step_7/updated_data.json', 'wt', encoding='utf-8') as file:
    json.dump(new_data, file)