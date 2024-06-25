time_table = [
    {"number": "CS101", "class": 3004, "teacher": "Хайнс", "time": "8:00"},
    {"number": "CS102", "class": 4501, "teacher": "Альварадо", "time": "9:00"},
    {"number": "CS103", "class": 6755, "teacher": "Рич", "time": "10:00"},
    {"number": "NT110", "class": 1244, "teacher": "Берк", "time": "11:00"},
    {"number": "CM241", "class": 1411, "teacher": "Ли", "time": "13:00"},
]
number = input()
for curs in time_table:
    if number in curs["number"]:
        print(f"{curs['number']}: {curs['class']}, {curs['teacher']}, {curs['time']}")
