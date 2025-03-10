from collections import defaultdict


def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    dict_matrix = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            dict_matrix[i + 1].append(matrix[i][j])
    return dict(dict_matrix)


matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

print(matrix_to_dict(matrix))

annotations = matrix_to_dict.__annotations__

print(annotations["return"])
