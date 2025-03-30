def filterfalse(predicate, iterable):
    if predicate == None:
        return [i for i in iterable if i not in filter(bool, iterable)]
    else:
        return filter(lambda el: not predicate(el), iterable)


objects = [0, 1, True, False, 17, []]

print(*filterfalse(None, objects))
