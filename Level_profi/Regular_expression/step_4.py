import re, sys

patern = r"^(\w+)\1$"
lines = sys.stdin.read().splitlines()

for line in lines:
    if re.fullmatch(patern, line):
        print(line)