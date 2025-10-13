import re

word = input().lower()
text = input().lower()

if word.endswith('ze'):
    british_version = word[:-2] + 'se'
    pattern = rf'\b({word}|{british_version})\b'
elif word.endswith('se'):
    american_version = word[:-2] + 'ze'
    pattern = rf'\b({word}|{american_version})\b'
else:
    pattern = rf'\b{re.escape(word)}\b'

matches = re.findall(pattern, text)
print(len(matches))