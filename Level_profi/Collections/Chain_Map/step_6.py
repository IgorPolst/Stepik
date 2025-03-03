from collections import ChainMap

def get_value(chainmap, key, from_left = True):
    if from_left:
        for el in chainmap.maps:
            if key in el.keys():
                return el[key]
    else:
        for el in chainmap.maps[::-1]:
            if key in el.keys():
                return el[key]

    return None

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name', False))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))