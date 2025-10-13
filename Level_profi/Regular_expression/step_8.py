import sys
import re

total_score = 0

for publication in sys.stdin:
    publication = publication.rstrip('\n')
    
    if not re.search(r'beegeek', publication, flags=re.I): continue
    else:  total_score += 1

print(total_score)