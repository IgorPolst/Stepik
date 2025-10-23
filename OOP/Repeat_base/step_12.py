def intersperse(iterable, delimiter):
    it = iter(iterable)
    
    try: yield next(it)
    except StopIteration: return
    for item in it:
        yield delimiter
        yield item