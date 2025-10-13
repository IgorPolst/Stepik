import re

def abbreviate(phrase):
    abbreviation = ''.join(re.findall(r'\b\w|[A-Z]', phrase))
    return abbreviation.upper()