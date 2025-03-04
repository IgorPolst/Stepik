import sys

lis = [i.strip() for i in sys.stdin]

total = 0
for el in lis:
    try:
        total = int(el)
    except ValueError:
        try:
            total = float(el)
        except:
            pass
print(int(el) if total % 1 == 0 else float(el))
