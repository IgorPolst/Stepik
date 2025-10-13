import sys

res = []
for el in sys.stdin:
    cordinate = eval(el.strip())
    res.append(-90 <= cordinate[0] <= 90 and -180 <= cordinate[1] <=180)
print(*res, sep="\n")

