from functools import reduce
names_file = {}
size = {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3}

with open("Repeat_base2/files.txt", "rt", encoding="utf-8") as file:
    lines = sorted(file.readlines())
    for line in lines: 
        name, size_number, size_degree =line.split()
        _, extension= name.split(".")
        names_file[extension] = names_file.setdefault(extension, [])
        names_file[extension].append(tuple([name, int(size_number)*size[size_degree]]))
        

names_file = {key: val for key, val in sorted(names_file.items(), key = lambda ele: ele[0])}
  
for ext in names_file.values():
    count = reduce(lambda result, file: result+file[1],ext, 0)
    num = [round(count/i[1]) if round(count/i[1]) < 1024 else 0 for i in size.items()]
    print(*map(lambda file: file[0],ext), sep = "\n")
    print("----------")
    print(f"Summary: {max(num)} {list(size)[num.index(max(num))]}\n")
