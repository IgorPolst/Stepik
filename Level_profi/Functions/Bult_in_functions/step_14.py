import sys

results = []
for el in sys.stdin:
    results.append(eval(el))
print(max(results))
