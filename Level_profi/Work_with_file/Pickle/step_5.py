import pickle

with open(input(), "rb") as file:
    data = pickle.load(file)

control_number = 0
if isinstance(data, dict):
    for key in data.keys():
        if isinstance(key, int):
            control_number += key
else:
    data = list(filter(lambda d: isinstance(d, int), data))
    control_number = max(data, default=0) * min(data, default=0)

res = int(input())
if res == control_number:
    print("Контрольные суммы совпадают")
else:
    print("Контрольные суммы не совпадают")
