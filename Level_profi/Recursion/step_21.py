def recursive_sum(nested_lists, value = 0):
    if nested_lists == []:
        return 0
    else:
        for el in nested_lists:
            if isinstance(el, list):
                return value + recursive_sum(el)
            else:
                return value + el
            
def recursive_sum(nested_lists, value=0):
    if nested_lists == []:
        return value
    else:
        for el in nested_lists:
            if isinstance(el, list):
                value = recursive_sum(el, value)
            else:
                value += el
    return value