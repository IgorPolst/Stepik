import string

new_dict = dict(zip([i for i in string.ascii_lowercase], [str(i) for i in input()]))
line = input()
tbl = line.maketrans(new_dict)
line.translate(tbl)

print(line)
