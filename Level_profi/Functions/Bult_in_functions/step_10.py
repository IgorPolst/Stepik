def zip_longest(*args, fill=None):
    max_len = max(len(i) for i in args)
    for lis in args:
        while len(lis) < max_len:
            lis.append(fill)
    return list(zip(*args))
