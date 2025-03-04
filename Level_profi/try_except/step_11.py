def add_to_list_in_dict(data, key, element):
    try:
        data[key].append(element)
    except:
        data[key] = data.setdefault(key, [])
        data[key].append(element)
    return None


data = {"a": [1, 2, 3], "b": [4, 5, 6]}
add_to_list_in_dict(data, "b", 7)

print(data)

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
add_to_list_in_dict(data, "c", 7)

print(data)
