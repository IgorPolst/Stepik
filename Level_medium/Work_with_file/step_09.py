def read_csv():
    with open("Work_with_file/data.csv", "rt") as file:
        key = file.readline().strip().split(",")
        data = []
        for line in file.readlines():
            data.append(dict(zip(key, line.strip().split(","))))
    return data


print(read_csv())
