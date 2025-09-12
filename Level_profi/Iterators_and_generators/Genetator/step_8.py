def unique(iterable: iter):
    unique_el = [el for el in iter if el not in unique_el]
    return iter(unique_el)
