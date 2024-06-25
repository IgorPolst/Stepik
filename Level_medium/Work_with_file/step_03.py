with open("C:/Users/Igor/Documents/GitHub/124_groupMPGU/Stepic/Level_medium/Work_with_file/text.txt", "rt") as file:
    line = file.readline()
    line = reversed(line)
    print(*line)