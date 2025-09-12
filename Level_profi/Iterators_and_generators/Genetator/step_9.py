def stop_on(iterable, obj):
    for el in iterable:
        if el == obj:
            break
        else:
            yield el
        