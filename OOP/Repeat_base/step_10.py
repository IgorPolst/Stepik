import re
def is_decimal(string):
    if not string.strip(): return False 
    pattern = r'^[-+]?(\d*\.\d+|\d+\.?\d*)$'
    return bool(re.match(pattern, string.strip()))
print(is_decimal('19'))