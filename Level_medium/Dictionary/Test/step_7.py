def merge(values):      # values - это список словарей
    all = {}
    for i in values:
        for key, value in i.items():
            all.setdefault(key,set()).add(value)
    return (all)