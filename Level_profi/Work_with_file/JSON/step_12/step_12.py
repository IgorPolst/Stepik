import csv, json

with open('Stepik/Level_profi/Work_with_file/JSON/step_12/students.json', 'rt', encoding='utf-8') as file:
    data = sorted(json.loads(file.read()), key= lambda student: student["name"])

with open('Stepik/Level_profi/Work_with_file/JSON/step_12/data.csv', 'wt', encoding='utf-8') as file:
    
    result = csv.DictWriter(file, ["name", "phone"], extrasaction= "ignore")

    result.writeheader()
    for student in data:  
        if(student['age'] >= 18 and student["progress"] >= 75):
            result.writerow(student)