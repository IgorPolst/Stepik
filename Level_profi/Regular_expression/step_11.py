import re

text = input()
word = input()
patern = r"\b" + re.escape(word) + r"\b"
print(len(re.findall(patern, text)))
