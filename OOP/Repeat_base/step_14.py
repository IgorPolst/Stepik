def pluck(data, path, default=None):
    keys = path.split('.')
    current = data
    
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]  
        else:
            return default 
    
    return current