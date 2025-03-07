def linear(nested_lists):
    result = [] 
    for el in nested_lists:
        if isinstance(el, list):  
            result.extend(linear(el))  
        else:
            result.append(el) 
    return result