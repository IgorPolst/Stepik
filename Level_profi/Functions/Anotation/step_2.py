def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    top_mark = max(grades["grades"])
    return {"name": grades["name"], "top_grade": top_mark}

info = {'name': 'Timur', 'grades': [30, 57, 99]}

print(top_grade(info))

annotations = top_grade.__annotations__

print(annotations['grades'])

print(*top_grade.__annotations__.values())