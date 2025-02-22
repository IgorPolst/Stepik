import json

with open(
    "Level_profi/Work_with_file/JSON/step_16/food_services.json", "rt", encoding="utf-8"
) as file:
    data = json.load(file)

type_object = {}

for object in data:
    type_object[object["TypeObject"]] = type_object.setdefault(object["TypeObject"], [])
    type_object[object["TypeObject"]].append(
        tuple([object["Name"], object["SeatsCount"]])
    )

type_object = sorted(type_object.items(), key=lambda object: object[0])


biggest_objects = dict(
    map(
        lambda object: tuple(
            [
                object[0],
                sorted(object[1], key=lambda restoran: restoran[1], reverse=True)[0],
            ]
        ),
        type_object,
    )
)
for biggest_object in biggest_objects.items():
    print(f"{biggest_object[0]}: {biggest_object[1][0]}, {biggest_object[1][1]}")
