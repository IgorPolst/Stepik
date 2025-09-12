def txt_to_dict():
    with open("Iterators_and_generators\Genetator\Part 3\planets.txt", "r", encoding="UTF-8") as file:
        planet = dict()
        all_lines = (line.strip().split("=") for line in file) 
        for line in all_lines:
            if line[0] != "":
                planet[line[0].strip()] = line[1].strip()
            else: 
                yield planet
                planet = dict()
        yield planet

planets = txt_to_dict()

print(next(planets))