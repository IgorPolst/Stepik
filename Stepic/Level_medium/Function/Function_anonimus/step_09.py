colors = [int(i) for i in input().split()]
print(*map(lambda color: 255 - color, colors))
