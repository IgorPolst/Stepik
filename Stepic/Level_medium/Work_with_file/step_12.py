with open("Work_with_file/input.txt", "rt") as reading_file, open("output.txt", "w") as writting_file:

    lines = reading_file.readlines()
    for i in range(len(lines)):
        print(f"{i+1}) {lines[i]}", end = "",file=writting_file)
