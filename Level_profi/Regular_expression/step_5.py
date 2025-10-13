import sys
import re

count_bee = 0
count_geek = 0

for line in sys.stdin:
    line = line.rstrip('\n')
    
    bee_count = line.count('bee')
    if bee_count >= 2:
        count_bee += 1
    
    if re.search(r'\bgeek\b', line, re.IGNORECASE):
        count_geek += 1

print(count_bee)
print(count_geek)