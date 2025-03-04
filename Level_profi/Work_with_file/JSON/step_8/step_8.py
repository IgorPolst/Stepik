import json

with open(
    "Stepik\Level_profi\Work_with_file\JSON\step_8\data1.json", "rt", encoding="utf-8"
) as file1, open(
    "Stepik\Level_profi\Work_with_file\JSON\step_8\data2.json", "rt", encoding="utf-8"
) as file2:
    data1 = json.loads(file1.read())
    data2 = json.loads(file2.read())

result_data = data1 | data2
print(result_data, sep="\n")
with open(
    "Stepik\Level_profi\Work_with_file\JSON\step_8\data_merge.json",
    "wt",
    encoding="utf-8",
) as file:
    json.dump(result_data, file)
