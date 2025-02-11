import json
import sys

data = json.loads(sys.stdin)
map(lambda parametr: print(parametr) ,data)