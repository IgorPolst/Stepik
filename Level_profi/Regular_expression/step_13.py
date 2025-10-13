import re

word = input().lower()
text = input().lower()

if 'our' in word:
    american_version = word.replace('our', 'or')
    pattern = rf'\b({word}|{american_version})\b'
else:
    pattern = rf'\b{word}\b'

matches = re.findall(pattern, text)
print(len(matches))