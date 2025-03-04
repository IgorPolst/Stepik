import csv

from collections import defaultdict


def condense_csv(filename, id_name):
    # Создаем словарь для хранения сгруппированных данных
    data = defaultdict(lambda: defaultdict(str))

    # Читаем данные из исходного CSV файла
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            # Разделяем данные на имя объекта, свойство и значение
            obj_name, prop_name, value = row

            # Сохраняем значение свойства в словаре
            data[obj_name][prop_name] = value

    # Получаем все свойства для заголовков
    all_properties = list()
    for obj in data.values():
        all_properties = obj.keys()

    # Записываем сгруппированные данные в новый CSV файл
    with open("condensed.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Записываем заголовок
        header = [id_name] + list(all_properties)
        writer.writerow(header)

        # Записываем строки с данными
        for obj_name, props in data.items():
            row = [obj_name] + [props.get(prop, "") for prop in all_properties]
            writer.writerow(row)


condense_csv("Stepik/Level_profi/Work_with_file/CSV/test.csv", id_name="ID")

with open("condensed.csv", encoding="utf-8") as file:
    print(file.read().strip())
