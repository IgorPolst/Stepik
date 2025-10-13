import sys
import re
from collections import defaultdict

html = sys.stdin.read()
tags = defaultdict(set)

for tag_match in re.finditer(r'<(\w+)([^>]*)>', html):
    tag_name = tag_match.group(1)
    attrs_string = tag_match.group(2)
    
    attrs = re.findall(r'([a-zA-Z][a-zA-Z0-9_-]*)\s*=', attrs_string)
    for attr in attrs:
        tags[tag_name].add(attr)

for tag in sorted(tags):
    attrs_str = ', '.join(sorted(tags[tag]))
    print(f"{tag}: {attrs_str}" if attrs_str else f"{tag}:")