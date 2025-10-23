import re

def is_fraction(string):
    pattern = r'^-?\d+/[1-9]\d*$'
    return bool(re.match(pattern, string))