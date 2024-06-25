with open(
    "C:/Users/Igor/Documents/GitHub/124_groupMPGU/Stepic/Level_medium/Work_with_file/lines.txt",
    "rt",
) as file:
    lines = file.readlines()
    lenth = len(max(lines, key=len))
    print(*filter(lambda line: len(line) == lenth, lines), sep="")
