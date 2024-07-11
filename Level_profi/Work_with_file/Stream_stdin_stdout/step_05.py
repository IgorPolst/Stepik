import sys

lines = [line.strip("\n").startswith("#") for line in sys.stdin]
print(lines)