import json
import sys

dates = json.loads(sys.stdin.read())
print(*(f'{k}: {", ".join(map(str, v))}' if isinstance(v, list) else f'{k}: {v}' 
    for k, v in dates.items()), sep='\n')