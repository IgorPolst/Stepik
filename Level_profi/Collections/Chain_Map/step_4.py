from collections import ChainMap


def deep_update(chainmap, key, value):
    if len(chainmap.maps) == 1 and len(chainmap.maps[0]) == 0:
        return None
    for el in chainmap.maps:
        if key in el.keys():
            el[key] = value
    chainmap.setdefault(key, value)
    return chainmap


chainmap = ChainMap({"city": "Moscow"}, {"name": "Arthur"}, {"name": "Timur"})
deep_update(chainmap, "name", "Dima")

print(chainmap)
