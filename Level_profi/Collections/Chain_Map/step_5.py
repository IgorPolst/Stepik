from collections import ChainMap


def deep_update(chainmap, key, value):
    for el in chainmap.maps:
        if key in el.keys():
            el[key] = value
    chainmap.setdefault(key, value)
    return None