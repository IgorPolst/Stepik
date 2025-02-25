from zipfile import ZipFile
import json

footbal_team = []
with ZipFile("Level_profi/Work_with_file/ZIP/step_9/data.zip", "r") as zip_file:
    zip_list = filter(lambda f: f.filename.split(".")[-1] == "json", zip_file.infolist())
    for file in zip_list:
        with zip_file.open(file, "r") as file:
            try:
               player = json.load(file)  
            except: 
                continue
        if(player["team"] == "Arsenal"):
                footbal_team.append(f'{player["first_name"]} {player["last_name"]}')
                
print(*sorted(footbal_team), sep="\n")

    