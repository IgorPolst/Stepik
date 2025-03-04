from collections import namedtuple
import pickle

Animal = namedtuple("Animal", ["name", "family", "sex", "color"])

with open("Level_profi/Collections/NamedTuple/step_3/data.pkl", "rb") as file:
    data = pickle.load(file)

for animal in data:
    for key, value in animal._asdict().items():
        print(f"{key}: {value}")
    print()
