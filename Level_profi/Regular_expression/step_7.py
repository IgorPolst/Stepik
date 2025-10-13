import re

text = input()
pattern = r'^(Здравствуйте|Доброе утро|Добрый день|Добрый вечер)'
result = bool(re.search(pattern, text, re.IGNORECASE))

print(result)