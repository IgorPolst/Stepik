def convert(string):
    up = 0
    down = 0
    for i in string:
        if i.isalpha():
            if i.isupper():
                up += 1
            else:
                down += 1
    if up > down:
        return string.upper()
    else:
        return string.lower()


print(convert("pyTHON"))
