def custom_isinstance(objects, typeinfo):
    return sum( 1 for i in objects if isinstance(i, typeinfo))