import re
print(*re.split(r"\s*and\s*|\s*or\s*|\s*[|&]\s*",input()), sep=", ")
