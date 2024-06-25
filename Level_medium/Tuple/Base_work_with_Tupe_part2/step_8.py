a, b, c = int(input()), int(input()), int(input())

x = -(b / (2 * a))
y = (4 * a * c - b**2) / (4 * a)
coordinates = [x, y]
print(tuple(coordinates))
