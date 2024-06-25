mult = set()
for i in input().split():
    if int(i) in mult:
        print("YES")
    else:
        mult.add(int(i))
        print("NO")
