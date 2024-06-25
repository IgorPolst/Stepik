with open(f"Exams/{input()}", "rt") as file:
    data = [line.strip() for line in file.readlines()]
print(data)
if len(data) < 10:
    print(*data, sep = "\n")
else: 
    print(*data[-10:], sep ="\n")