with open("Work_with_file/goats.txt", "rt") as goats, open("Work_with_file/answer.txt", "wt") as answer:
    line = ""
    while line != "GOATS\n":
        line = goats.readline()
    total = {}
    goats_list = goats.readlines()
    for line in goats_list:    
        total[line.strip()]= total.setdefault(line.strip(),0)+1
    res = list(filter(lambda goat: int(goat[1]/len(goats_list)*100) > 7, total.items()))
    for el in res: 
        answer.write(f"{el[0]}\n")


