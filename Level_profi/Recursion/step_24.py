def get_all_values(nested_dicts, key):
    result = set() 
    
    if isinstance(nested_dicts, dict):
        if key in nested_dicts: 
            result.add(nested_dicts[key])      
       
        for value in nested_dicts.values():
            result.update(get_all_values(value, key))

    return result  