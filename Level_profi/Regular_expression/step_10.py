import re

text = input()
word = input()
patern = r"(?<=\w)" + re.escape(word) + r"(?=\w)"
print(len(re.findall(patern, text)))
