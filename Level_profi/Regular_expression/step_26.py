import re

def multiple_split(string, delimeters):
    escaped_delims = [re.escape(d) for d in delimeters]
    delimeter_patern = fr"\s*(?:{'|'.join(escaped_delims)})\s*"
    return re.split(delimeter_patern, string)

print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))