def print_operation_table(operation, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(operation(i, j), end=" ")
        print()
