from collections import defaultdict

def flip_dict(dict_of_lists):
    favorite_drink = defaultdict(list)
    for human in dict_of_lists.items():
        for drink in human[1]:
            favorite_drink[drink].append(human[0])
    return favorite_drink


data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')