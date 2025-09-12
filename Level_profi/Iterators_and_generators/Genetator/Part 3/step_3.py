def filter_names(names, ignore_char, max_names):
    without_ignor_char = (name for name in names if name[0].lower() != ignore_char.lower())
    without_number = (name for name in without_ignor_char if not any(char.isdigit() for char in name))
    yield from (name for i, name in enumerate(without_number) if i < max_names)


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 3))

