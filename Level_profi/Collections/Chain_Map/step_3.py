from collections import ChainMap

def get_all_values(chainmap, key):
        return set(el[key] for el in chainmap.maps if key in el.keys())
 
    
chainmap = ChainMap({'name': 'Anri'}, {'name': 'Arthur', 'age': 20}, {'name': 'Timur', 'age': 29})
result = get_all_values(chainmap, 'age')

print(*sorted(result))