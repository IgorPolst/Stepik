x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 + x2 + y1 + y2) % 2 == 1 and x1 != x2 and y1 != y2:
    print("YES")
else:
    print("NO")
