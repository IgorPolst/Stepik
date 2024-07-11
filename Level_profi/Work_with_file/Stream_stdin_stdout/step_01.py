import sys
print(*[line[::-1].strip("\n") for line in sys.stdin], sep = "\n")
