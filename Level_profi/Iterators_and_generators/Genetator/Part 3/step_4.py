
with open("Iterators_and_generators\Genetator\Part 3\data.csv", "r", encoding="UTF-8") as file:
    file_lines = (line for line in file)
    lines_values = (line.rstrip().split(",") for line in file_lines)
    round_a = (int(line[1]) for line in lines_values if line[2] == 'a')
    print(sum(round_a))