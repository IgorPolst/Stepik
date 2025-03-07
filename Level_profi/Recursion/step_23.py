def find_key(data, key):
    if key in data:
        return data[key]                # базовый случай
    
    for v in data.values():
        if type(v) == dict:
            value = find_key(v, key)    # рекурсивный случай
            if value is not None:
                return value 