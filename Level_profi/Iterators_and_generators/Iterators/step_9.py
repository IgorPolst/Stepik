def is_iterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False


print(is_iterable(iter([1, 2, 3, 4])))
