
file_name = open("C:/Users/Igor/Documents/GitHub/124_groupMPGU/Stepic/Level_medium/Work_with_file/prices.txt", "rt")
file = file_name.readlines()
file_name.close()
total = 0
for string in file:
    elements = string.split()
    total += int(elements[1])*int(elements[2])
print (total)


