import re
import sys

patern = r"^_\d+[A-Za-z]*_?$"
lines = sys.stdin.read().splitlines()
for line in lines:
    if re.fullmatch(patern, line): print("True")
    else: print("False")