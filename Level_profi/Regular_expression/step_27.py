import re

a,b = map(int, input().split())
patern = re.compile(r"\d+")

print(sum(map(int, patern.findall(input(),pos = a, endpos = b))))
