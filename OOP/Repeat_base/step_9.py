import re
def is_integer(string):
    pattern = r"^[-+]?\d+$"
    return bool(re.match(pattern, string.strip()))
print(is_integer('19.1'))