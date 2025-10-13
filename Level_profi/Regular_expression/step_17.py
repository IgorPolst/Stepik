import re
def normalize_jpeg(text):
    return re.sub(r"\.\w{3,4}$",lambda el: el.group().lower(),text)