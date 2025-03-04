import csv
from collections import Counter

with open(
    "Level_profi/Collections/Counter/step_12/name_log (1).csv", "rt", encoding="utf-8"
) as file:
    data = csv.DictReader(file)
    emails = Counter(map(lambda user: user["email"], data))
for key, values in sorted(emails.items()):
    print(f"{key}: {values}")
