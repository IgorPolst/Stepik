from collections import defaultdict


data = [
    ("Books", 1343),
    ("Books", 1166),
    ("Merch", 616),
    ("Courses", 966),
    ("Merch", 1145),
    ("Courses", 1061),
    ("Books", 848),
    ("Courses", 964),
    ("Tutorials", 832),
    ("Merch", 642),
    ("Books", 815),
    ("Tutorials", 1041),
    ("Books", 1218),
    ("Tutorials", 880),
    ("Books", 1003),
    ("Merch", 951),
    ("Books", 920),
    ("Merch", 729),
    ("Tutorials", 977),
    ("Books", 656),
]

new_data = defaultdict(int)
for product in data:
    new_data[product[0]] += product[1]

for key, value in sorted(new_data.items()):
    print(f"{key}: ${value}")
