import keyword
import re

# keyword_list = keyword.kwlist 
keyword_list = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

text = input()
patern = fr"\b({'|'.join(map(re.escape, keyword_list))})\b"
print(re.sub(patern, "<kw>", text, flags=re.I))