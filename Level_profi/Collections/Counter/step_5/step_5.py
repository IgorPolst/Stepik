from collections import Counter

with open("Level_profi/Collections/Counter/step_5/pythonzen.txt", "rt", encoding="utf-8") as file:
    data = Counter(file.read().lower())

for key, value in sorted(data.items()):
    if key.isalpha():
        print(f"{key}: {value}")