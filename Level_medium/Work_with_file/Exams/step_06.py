with open(f"Exams/{input()}", "rt", encoding="utf-8") as infile: 
    cod = infile.read().strip().split("\n")

cod = list(filter(lambda line:line[:3] == "def" or line[0:1] == "#" ,cod))
pre_line = ""
res = []
for line in cod:
    if line.startswith("def") and not pre_line.startswith("#"):
        res.append(line)
    pre_line = line
if res == []:
    print("Best Programming Team")
else: 
    print(*map(lambda strin: strin[3:strin.find("(")].strip(),res), sep = "\n")