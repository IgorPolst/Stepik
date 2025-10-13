import re

text = input()
pattern = r'(\b\w+\b)(\W+\1\b)+'
result = re.sub(pattern, r'\1', text)

print(result)