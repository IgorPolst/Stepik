import sys
import re

total_score = 0

for publication in sys.stdin:
    publication = publication.rstrip('\n')
    
    if not re.search(r'beegeek', publication): continue
    starts_with = re.match(r'^beegeek', publication) is not None
    ends_with = re.search(r'beegeek$', publication) is not None
    
    if starts_with and ends_with:
        total_score += 3
    elif starts_with or ends_with:
        total_score += 2
    else:
        total_score += 1

print(total_score)