import sys
from datetime import date

data = [date.fromisoformat(line.strip("\n")) for line in sys.stdin]
print((max(data) - min(data)).days)
