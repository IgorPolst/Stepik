from random import choice

with open("Work_with_file/first_names.txt", "rt") as file_name, open(
    "Work_with_file/last_names.txt", "rt"
) as file_sername:
    names = file_name.readlines()
    sernames = file_sername.readlines()

for _ in range(3):
    print(f"{choice(names).strip()} {choice(sernames).strip()}", sep=" ")
