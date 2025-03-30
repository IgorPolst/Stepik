def transpose(matrix):
    return [list(i) for i in zip(*matrix)]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in transpose(matrix):
    print(row)
