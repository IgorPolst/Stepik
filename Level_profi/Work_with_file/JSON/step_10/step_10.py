import json

with open(
    "Stepik\Level_profi\Work_with_file\JSON\step_10\countries.json",
    "rt",
    encoding="utf-8",
) as file:
    data = json.loads(file.read())

religion = dict()
for town in data:
    religion.setdefault(town["religion"], []).append(town["country"])

print(religion)
with open(
    "Stepik/Level_profi/Work_with_file/JSON/step_10/religion.json",
    "wt",
    encoding="utf-8",
) as file:
    json.dump(religion, file, indent=3, separators=(",", ":"))
