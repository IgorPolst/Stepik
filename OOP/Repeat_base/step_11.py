import re
def is_fraction(string):
    if not string.strip(): return False 
    pattern = r'^[-+]?(0|[1-9]\d+)\/([1-9]\d*)$'
    return bool(re.match(pattern, string.strip()))