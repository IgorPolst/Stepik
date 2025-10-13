import re

def decode_string(s):
    if '(' not in s:
        return s
    
    pattern = r'(\d+)\(([^()]+)\)'
    
    while True:
        match = re.search(pattern, s)
        if not match:
            break
        
        replacement = match.group(2) * int(match.group(1))
        s = s[:match.start()] + replacement + s[match.end():]
    return decode_string(s)
 
print(decode_string(input()))