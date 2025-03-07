def dict_travel(nested_dicts, parent_key=''):
    
    for key in sorted(nested_dicts.keys()):
        full_key = f"{parent_key}.{key}" if parent_key else key  

        if isinstance(nested_dicts[key], dict):  
            dict_travel(nested_dicts[key], full_key)  
        else:
            print(f"{full_key}: {nested_dicts[key]}")