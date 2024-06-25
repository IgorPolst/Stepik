with open("Work_with_file/population.txt", "rt") as file:
    population = file.readlines()

towns = [
    [town.split("\t")[0], int(town.split("\t")[1].strip("\n"))] for town in population
]
towns = list(filter(lambda town: town[0][0] == "G" and town[1] > 500000, towns))
for town in towns:
    print(town[0])
