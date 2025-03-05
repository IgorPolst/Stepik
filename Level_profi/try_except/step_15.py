import json

data_name = input()

try:
    with open(data_name, "rt", encoding="utf-8") as file:
        data = json.dump(file)
    print(data)
except FileNotFoundError:
    print("Файл не найден") 
except Exception:
    print("Ошибка при десериализации") 