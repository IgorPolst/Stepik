def get_min_max(data):
    if len(data) > 0:
        return tuple([data.index(min(data)), data.index(max(data))])
    else:
        return None


data = [2, 3, 8, 1, 7]

print(get_min_max(data))
