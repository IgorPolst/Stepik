import json
from collections import ChainMap
with open("Level_profi\Collections\Chain_Map\step_1\zoo.json","rt", encoding="utf-8") as file:
    print(sum(ChainMap(*json.load(file)).values()))
