file_name = open(
    "C:/Users/Igor/Documents/GitHub/124_groupMPGU/Stepic/Level_medium/Work_with_file/nums.txt",
    "rt",
)
file = file_name.read().split()
print(int(file[0]) + int(file[1]))
file_name.close()
