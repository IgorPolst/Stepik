with open("Work_with_file\class_scores.txt", "rt") as reading_file, open("Work_with_file/new_scores.txt", "wt") as w_file:
    for line in reading_file:
        elements = line.strip().split()
        if int(elements[1]) <= 95:
            elements[1] = 5+int(elements[1])
        else:
            elements[1] = 100
        print(*elements, file=w_file)
        