a, b, c = len(input()), len(input()), len(input())

maxn = max(a, b, c)
minn = min(a, b, c)
sred = a + b + c - maxn - minn

if maxn - sred == sred - minn:
    print("YES")
else:
    print("NO")
